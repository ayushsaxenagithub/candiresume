from django.contrib import admin
from .models import Candidate, Project,Skill
# Register your models here.

admin.site.register(Candidate)
admin.site.register(Skill)
admin.site.register(Project)
