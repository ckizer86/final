# Generated by Django 2.2 on 2021-06-07 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='amount',
        ),
        migrations.AddField(
            model_name='user',
            name='total',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
