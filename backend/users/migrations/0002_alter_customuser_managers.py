# Generated by Django 3.2.6 on 2021-08-24 11:47

from django.db import migrations
import users.managers


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', users.managers.CustomUserManager()),
            ],
        ),
    ]
