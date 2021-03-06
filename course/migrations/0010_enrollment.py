# Generated by Django 3.1.4 on 2021-02-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_course_comment_course_comment_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=250)),
                ('user_email', models.CharField(max_length=250)),
                ('enroll', models.BooleanField()),
                ('status', models.CharField(choices=[('completed', 'completed'), ('incomplete', 'incomplete')], max_length=250)),
            ],
        ),
    ]
