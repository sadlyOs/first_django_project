# Generated by Django 4.0.5 on 2022-07-19 06:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_project_project2'),
    ]

    operations = [
        migrations.AddField(
            model_name='project2',
            name='data',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
