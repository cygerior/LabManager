# Generated by Django 3.2.5 on 2021-07-15 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ConfManager', '0019_remove_board_interfaces'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BoardInterface',
        ),
    ]
