# Generated by Django 4.0.4 on 2022-07-29 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0005_client_direction_client_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='direction',
        ),
        migrations.AddField(
            model_name='client',
            name='first_name',
            field=models.CharField(default=None, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='rol',
            field=models.CharField(default='client', editable=False, max_length=40),
        ),
    ]
