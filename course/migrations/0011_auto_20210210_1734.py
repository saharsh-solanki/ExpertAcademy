# Generated by Django 3.1.4 on 2021-02-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_enrollment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='course_name',
            new_name='course_id',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='enroll',
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('completed', 'completed'), ('incomplete', 'incomplete')], default='incomplete', max_length=250),
        ),
    ]