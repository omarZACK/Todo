from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..models import TagModel
from ..serializers import TagSerializer
from django.db.models import Q
from django.db import transaction

class TagViewSet(ModelViewSet):
    queryset = TagModel.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(
            Q(created_by=self.request.user) |
            Q(users__id=self.request.user.id)
        ).distinct()

    def perform_create(self, serializer):
        name = serializer.validated_data['name'].lower()
        tag, created = TagModel.objects.get_or_create(
            name__iexact=name,
            defaults={
                'name': name,
                'created_by': self.request.user
            }
        )
        tag.users.add(self.request.user)
        serializer.instance = tag

    def destroy(self, request, *args, **kwargs):
        tag = self.get_object()

        # Case 1: User is not the creator - just remove from M2M
        if tag.created_by != request.user:
            tag.users.remove(request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)

        # Case 2: User is the creator and others use the tag
        if tag.users.exclude(id=request.user.id).exists():
            tag.users.remove(request.user)
            # Optionally transfer creator rights if needed
            # new_creator = tag.users.first()
            # tag.created_by = new_creator
            # tag.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        # Case 3: User is creator and no one else uses the tag - delete completely
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        with transaction.atomic():
            instance = self.get_object()
            new_name = request.data.get('name', '').strip().lower()

            # Case 1: User is creator and no one else uses the tag
            if instance.created_by == request.user and not instance.users.exclude(id=request.user.id).exists():
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)

            # Case 2 & 3: Either creator with other users or non-creator
            # Try to find existing tag with new name
            existing_tag = TagModel.objects.filter(
                Q(name__iexact=new_name) |
                Q(name__iexact=new_name.lower()) |
                Q(name__iexact=new_name.capitalize())
            ).first()

            if existing_tag:
                # Link user to existing tag
                existing_tag.users.add(request.user)
                serializer = self.get_serializer(existing_tag)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # Create new tag
                new_tag = TagModel.objects.create(
                    name=new_name,
                    created_by=request.user
                )
                new_tag.users.add(request.user)
                serializer = self.get_serializer(new_tag)
                return Response(serializer.data, status=status.HTTP_201_CREATED)