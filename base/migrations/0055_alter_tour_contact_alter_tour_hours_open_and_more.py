# Generated by Django 4.0.5 on 2022-07-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0054_tour_instructions_tour_places_nearby_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='contact',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='tour',
            name='hours_open',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='tour',
            name='instructions',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='tour',
            name='places_nearby',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='tour',
            name='website',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
