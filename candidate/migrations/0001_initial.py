# Generated by Django 3.2.5 on 2022-05-13 13:50

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('short_intro', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=2000, null=True)),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, default=1, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('social_github', models.URLField(blank=True, null=True)),
                ('social_linkedin', models.URLField(blank=True, null=True)),
                ('social_website', models.URLField(blank=True, null=True)),
                ('social_twitter', models.URLField(blank=True, null=True)),
                ('social_youtube', models.URLField(blank=True, null=True)),
                ('social_facebook', models.URLField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('Description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='candidate.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('demo_link', models.URLField(blank=True, null=True)),
                ('source_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidate.candidate')),
                ('tags', models.ManyToManyField(blank=True, to='candidate.Tag')),
            ],
        ),
    ]
