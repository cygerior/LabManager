# Generated by Django 3.1.3 on 2020-12-11 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IPLabo', '0004_remove_ippool_arp_mac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arp',
            name='ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPLabo.ippool'),
        ),
    ]
