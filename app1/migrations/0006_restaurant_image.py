# Generated by Django 5.0.1 on 2024-04-22 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_restaurant_remove_fooditem_restaurant_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
