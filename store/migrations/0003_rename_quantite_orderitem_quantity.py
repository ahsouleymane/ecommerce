# Generated by Django 3.2.12 on 2022-06-23 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quantite',
            new_name='quantity',
        ),
    ]