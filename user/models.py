from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pictures")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kawrgs):
        """
        Override save method to process profile image.
        """
        super().save(*args, **kawrgs)
        try:

            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_img = (300, 300)
                img.thumbnail(output_img)
                img.save(self.image.path)
        except Exception as e:
            print(f"Error processing profile image: {e}")
