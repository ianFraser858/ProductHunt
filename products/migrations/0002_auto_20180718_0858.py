# Generated by Django 2.0.7 on 2018-07-18 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_url',
            field=models.URLField(),
        ),
    ]