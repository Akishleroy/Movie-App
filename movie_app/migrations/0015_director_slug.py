# Generated by Django 4.1.2 on 2022-11-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0014_remove_movie_actor_movie_actors'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]