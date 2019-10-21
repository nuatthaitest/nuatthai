from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Services(models.Model):
    MY_CHOICES = (
        (350, 'Nuat Thai Foot Massage(1hour)'),
        (350, 'Thai Body massage w/ Oil(1hour)'),
        (400, 'Sweddish Massage(1hour)'),
        (400, 'Armoatherapy Massage(1hour)'),
        (250, 'Express - Back and Head(30 mins)'),
        (250, 'Foot Massage(30 mins)'),
        (250, 'Back Massage(30 mins)'),
        (250, 'Head massage(30 mins)'),
    )

    price = models.IntegerField(default=0)
    service = models.CharField(max_length=1, choices=MY_CHOICES)
