# Generated by Django 3.1.3 on 2020-12-11 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IPLabo', '0003_auto_20201108_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ippool',
            name='arp_mac',
        ),
    ]
