# Generated by Django 3.2.5 on 2022-05-15 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0010_alter_project_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/blank.png', null=True, upload_to='candidate_profile/'),
        ),
    ]