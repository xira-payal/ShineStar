# Generated by Django 4.2.6 on 2023-12-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
