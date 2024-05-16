# Generated by Django 4.1.7 on 2023-03-25 12:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_profile_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0008_paymentdetails_payment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('productname', 'user')},
        ),
    ]
