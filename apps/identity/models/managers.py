from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.
    """
    def create_user(self, email, name, password=None,gender=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.gender = gender
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        """
        Create and return a superuser with an email, username, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser creation failed: the user must have staff privileges.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser creation failed: the user must have superuser permissions.')

        return self.create_user(email, name, password, **extra_fields)