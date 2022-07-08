# Generated by Django 4.0.5 on 2022-06-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_tour_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dummylatlng',
            name='latLng',
        ),
        migrations.AddField(
            model_name='dummylatlng',
            name='lat',
            field=models.DecimalField(decimal_places=15, max_digits=20),
        ),
        migrations.AddField(
            model_name='dummylatlng',
            name='lng',
            field=models.DecimalField(decimal_places=15, max_digits=20),
        ),
    ]
