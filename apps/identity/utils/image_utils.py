from PIL import Image
import os
from django.conf import settings

def resize_image(image_path, size=(300, 300)):
    """Resize an image to the given size."""
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure consistent format
    img.thumbnail(size)
    img.save(image_path)

def get_default_avatar_path():
    """Return the default avatar image path."""
    return os.path.join(settings.STATIC_URL, 'images/default-avatar.png')

def is_valid_image(file):
    """Simple check for valid image extensions."""
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    ext = os.path.splitext(file.name)[1]
    return ext.lower() in valid_extensions
