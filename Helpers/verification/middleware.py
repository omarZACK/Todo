import json
from .models import VerificationCode

class VerificationCodeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Only act if signup just created a new user and response is JSON
        if (hasattr(request, 'user') and response.get('Content-Type') == 'application/json'
                and not request.user.is_active):
            try:
                # Get code for that user
                code = VerificationCode.objects.get(user_id=request.user.id)

                # Decode JSON content (bytes) to string and parse it
                content = json.loads(response.content.decode('utf-8'))

                # Add code to the response data
                content['code'] = code.code

                # Convert back to JSON string and set as response content
                updated_content = json.dumps(content)
                response.content = updated_content

                # Update Content-Length header
                response['Content-Length'] = str(len(updated_content))

            except (VerificationCode.DoesNotExist, json.JSONDecodeError) as e:
                print(f"Middleware error: {e}")

        return response
