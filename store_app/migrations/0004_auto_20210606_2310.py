# Generated by Django 2.2 on 2021-06-07 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0003_auto_20210606_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]