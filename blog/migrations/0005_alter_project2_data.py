# Generated by Django 4.0.5 on 2022-07-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_project2_data_alter_project2_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project2',
            name='data',
            field=models.CharField(max_length=100),
        ),
    ]
