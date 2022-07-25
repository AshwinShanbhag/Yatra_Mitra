# Generated by Django 4.0.5 on 2022-07-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_alter_tour_destination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='destination',
        ),
        migrations.AddField(
            model_name='tour',
            name='name',
            field=models.CharField(choices=[('1', 'Bangalore'), ('2', 'Dakshina Kannada'), ('3', 'Udupi'), ('4', 'Uttara Kannada')], default='1', max_length=1),
        ),
    ]
