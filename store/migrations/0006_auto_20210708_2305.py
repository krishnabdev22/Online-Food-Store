# Generated by Django 3.2.4 on 2021-07-08 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
    ]
