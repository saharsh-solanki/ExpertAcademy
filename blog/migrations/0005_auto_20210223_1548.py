# Generated by Django 3.1.4 on 2021-02-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210223_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_photo',
            field=models.ImageField(blank=True, upload_to='blog_image/'),
        ),
    ]
