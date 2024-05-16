# Generated by Django 4.1.7 on 2023-03-25 12:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_remove_profile_status'),
        ('customer', '0009_alter_cart_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'productname')},
        ),
    ]
