# Generated by Django 2.2 on 2020-11-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csmApp', '0014_auto_20201104_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='buy_price',
            field=models.FloatField(blank=True, null=True, verbose_name='采购价格'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='sale_price',
            field=models.FloatField(verbose_name='销售价格'),
        ),
    ]