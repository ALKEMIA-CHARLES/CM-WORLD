from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.dispatch import receiver
from django.db.models.signals import post_save
from pyuploadcare.dj.models import ImageField
# Create your models here.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("=========================================[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]=")

    if created:
        Profile.objects.create(user=instance)
        print("==========================================")


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="pictures")
    bio = models.CharField(max_length=250, null=True)
    age = models.IntegerField(null=True)


class Post(models.Model):
    image = models.ImageField(default="default.jpg", upload_to="pictures")
    title = models.CharField(max_length=70)
    message = models.TextField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    masterpost = models.ForeignKey(User, on_delete=models.CASCADE, null=True)