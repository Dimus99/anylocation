# Generated by Django 4.0.1 on 2022-02-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_page_producttype_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
