# Generated by Django 4.1.2 on 2022-11-22 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('D', 'Dollars'), ('R', 'Rubles'), ('E', 'Euro')], default='R', max_length=3),
        ),
    ]
