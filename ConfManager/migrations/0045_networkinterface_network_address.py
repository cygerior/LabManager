# Generated by Django 3.2.5 on 2021-10-17 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ConfManager', '0044_remove_networkinterface_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkinterface',
            name='network_address',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ConfManager.networkaddress'),
        ),
    ]
