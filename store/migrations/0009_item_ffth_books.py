# Generated by Django 4.1.7 on 2023-09-06 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_category'),
        ('store', '0008_laptop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_FFTH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='item_images')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='accounts.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='item_images')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_cat', to='accounts.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
