from django.db import models
from ckeditor.fields import RichTextField
import uuid
from django.utils import timezone


# Create your models here.
class Candidate(models.Model): 
    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100,null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=500,null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    short_intro = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=2000, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True,default='images/blank.png',upload_to='candidate_profile/')
    bio=RichTextField(null=True, blank=True)  
    status=models.IntegerField(null=True, blank=True, default=1) 
    created = models.DateTimeField(default=timezone.now)
    social_github = models.URLField(null=True, blank=True)
    social_linkedin = models.URLField(null=True, blank=True)
    social_website = models.URLField(null=True, blank=True)
    social_twitter = models.URLField(null=True, blank=True)
    social_youtube = models.URLField(null=True, blank=True)
    social_facebook = models.URLField(null=True, blank=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True , primary_key=True, editable=False)
    resume = models.FileField(null=True, blank=True, upload_to='doc')
    def __str__(self):
        return str(self.first_name)
    

    

class Skill(models.Model):
    owner = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return str(self.name)



class Project(models.Model):
    owner =  models.ForeignKey(Candidate,null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True)
    demo_link = models.URLField(null=True, blank=True)
    source_link = models.URLField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default-image.png", upload_to='project_image/')
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(null=True, blank=True,default=timezone.now)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    def __str__(self):
        return  self.title

class Tag(models.Model):
    pass

    def __str__(self):
        return self.name