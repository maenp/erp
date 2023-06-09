# Generated by Django 2.2 on 2020-11-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csmApp', '0018_auto_20201110_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='client_man',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='联系人'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='client_tel',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='client',
            field=models.CharField(max_length=50, verbose_name='客户'),
        ),
    ]
