# Generated by Django 2.2 on 2020-11-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csmApp', '0016_auto_20201108_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='order_finish',
            field=models.BooleanField(default=False),
        ),
    ]
