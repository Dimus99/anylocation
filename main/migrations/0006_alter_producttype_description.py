# Generated by Django 4.0.1 on 2022-02-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_producttype_product_producttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
