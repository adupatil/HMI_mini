from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(blank=True,upload_to='profile_pics')
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

    
    # def save(self,*args,**kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 100 or img.width > 100:
    #         output_size = (170,140)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)