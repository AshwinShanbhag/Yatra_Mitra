# Generated by Django 4.0.5 on 2022-07-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_alter_tour_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='place',
            field=models.CharField(choices=[('1', 'Bangalore'), ('2', 'Dakshina Kannada'), ('3', 'Udupi'), ('4', 'Uttara Kannada')], default='1', max_length=1),
        ),
    ]
