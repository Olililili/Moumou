from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Profile(models.Model):
    ANIMAL_CHOICES = [
        ('CAT', 'Cat'),
        ('DOG', 'Dog'),
        ('BUNNY', 'Bunny'),
        ('BIRD', 'Bird'),
    ]
    animal_type = models.CharField(
        "I am a: ",
        max_length=32,
        choices=ANIMAL_CHOICES,
        default='CAT',
    )

    name = models.CharField("My name is: ", max_length=240, null=True)

    FRIENDS_OR_LOVE_CHOICES = [
        ('FRIENDS', 'Friends'),
        ('LOVE', 'Love'),
    ]
    friend_or_love = models.CharField(
        "I am looking for: ",
        max_length=32,
        choices=FRIENDS_OR_LOVE_CHOICES,
        default='FRIENDS',
    )

    avatar1 = models.ImageField(upload_to='static/images/avatars', null=True)
    avatar_thumbnail = ImageSpecField(source='avatar1',
                                      processors=[ResizeToFill(40, 20)],
                                      format='JPEG',
                                      options={'quality': 60})

    def __str__(self):
        return self.name
