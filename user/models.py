from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    username=models.CharField(max_length=500,blank=True,null=True)
    email=models.EmailField(max_length=500, blank=True,null=True)
    image_profile=models.ImageField(null=True, blank=True, default='blank.png',upload_to='user_profile/')
    detail=models.TextField(blank=True,null=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True , primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

    @receiver(post_save, sender=User) 
    def create_user_profile(sender, instance, created, **kwargs):
	    if created:
		    Profile.objects.create(user=instance)

    @receiver(post_save, sender=User) 
    def save_user_profile(sender, instance, **kwargs):
	    instance.profile.save()

