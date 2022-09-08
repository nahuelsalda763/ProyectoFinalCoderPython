# Generated by Django 4.0.4 on 2022-08-04 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'coment', 'verbose_name_plural': 'comentarios'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='client',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
