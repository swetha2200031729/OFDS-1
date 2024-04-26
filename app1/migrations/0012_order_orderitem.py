# Generated by Django 5.0.1 on 2024-04-26 10:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_userphone_phone_cartitem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_placed_time', models.DateTimeField(blank=True)),
                ('delivary_name', models.CharField(max_length=100)),
                ('delivary_phone', models.CharField(max_length=100)),
                ('delivary_address', models.TextField()),
                ('fooditem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.fooditem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('fooditem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.fooditem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.order')),
            ],
        ),
    ]