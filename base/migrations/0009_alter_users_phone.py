# Generated by Django 4.0.5 on 2022-07-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_users_country_users_mail_users_state_alter_users_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
