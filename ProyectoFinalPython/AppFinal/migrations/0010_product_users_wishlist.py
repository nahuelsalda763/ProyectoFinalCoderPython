# Generated by Django 4.0.4 on 2022-08-02 17:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppFinal', '0009_remove_coments_client_coments_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='users_wishlist',
            field=models.ManyToManyField(blank=True, related_name='user_wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
