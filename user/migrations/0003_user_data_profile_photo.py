# Generated by Django 3.1.4 on 2021-02-20 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210126_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='profile_photo',
            field=models.ImageField(blank=True, default='profile_img/icon_male.png', null=True, upload_to='profile_img/'),
        ),
    ]
