# Generated by Django 4.0.4 on 2022-07-28 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppFinal', '0003_alter_client_options_alter_client_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={},
        ),
        migrations.AlterModelManagers(
            name='client',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='client',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='rol',
            field=models.CharField(default='client', max_length=40),
        ),
    ]