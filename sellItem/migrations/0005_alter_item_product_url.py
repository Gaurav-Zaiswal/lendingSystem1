# Generated by Django 3.2.7 on 2021-10-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellItem', '0004_item_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='product_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
