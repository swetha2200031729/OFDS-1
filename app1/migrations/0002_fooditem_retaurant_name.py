# Generated by Django 5.0.1 on 2024-04-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='retaurant_name',
            field=models.CharField(default="Anu's Kitchen", max_length=50),
        ),
    ]