from dataclasses import field
from django.forms import ModelForm
from .models import Candidate, Skill, Project
from django import forms

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone', 'short_intro',
        'location', 'profile_image', 'bio','social_github', 'social_linkedin',
        'social_website', 'social_twitter', 'social_youtube', 'social_facebook', 'resume' ]
        # fields='__all__'
        widget = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'featured_image', 'created_at', ]


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']