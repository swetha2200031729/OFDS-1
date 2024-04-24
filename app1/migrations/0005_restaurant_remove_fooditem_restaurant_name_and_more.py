# Generated by Django 5.0.1 on 2024-04-22 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_restaurent_name_fooditem_restaurant_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='restaurant_name',
        ),
        migrations.AddField(
            model_name='fooditem',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.restaurant'),
        ),
    ]
