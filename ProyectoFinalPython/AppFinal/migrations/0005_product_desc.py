# Generated by Django 4.0.5 on 2022-08-03 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0004_alter_product_options_alter_product_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]