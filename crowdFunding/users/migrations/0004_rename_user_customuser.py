# Generated by Django 5.0.3 on 2024-04-10 20:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_mobile_phone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='CustomUser',
        ),
    ]
