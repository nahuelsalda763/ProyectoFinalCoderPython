# Generated by Django 4.0.5 on 2022-07-27 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagen',
            field=models.ImageField(default='media/producto_image/coca.png', upload_to='producto_image'),
        ),
    ]