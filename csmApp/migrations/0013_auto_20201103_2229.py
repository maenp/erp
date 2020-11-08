# Generated by Django 2.2 on 2020-11-03 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csmApp', '0012_goodsinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='buy_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='采购价格'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='specification',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='规格/型号'),
        ),
    ]