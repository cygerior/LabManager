# Generated by Django 4.1 on 2022-09-01 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ConfManager', '0004_alter_interface_polymorphic_ctype_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='powersupply',
            options={'ordering': ['controller__name', 'port_number'], 'verbose_name_plural': 'Power supplies'},
        ),
    ]
