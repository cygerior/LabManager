# Generated by Django 3.1.7 on 2021-04-04 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ConfManager', '0010_board_interfaces'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkInterface',
            fields=[
                ('interface_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ConfManager.interface')),
                ('mac_address', models.CharField(max_length=23)),
                ('address', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('ConfManager.interface',),
        ),
        migrations.CreateModel(
            name='UartInterface',
            fields=[
                ('interface_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ConfManager.interface')),
                ('uri', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('ConfManager.interface',),
        ),
    ]
