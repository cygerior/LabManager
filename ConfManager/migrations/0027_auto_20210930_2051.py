# Generated by Django 3.2.5 on 2021-09-30 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConfManager', '0026_device_type'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='device',
            name='unique_target_device',
        ),
        migrations.RemoveField(
            model_name='device',
            name='name',
        ),
        migrations.AddConstraint(
            model_name='device',
            constraint=models.UniqueConstraint(fields=('board_id', 'type_id'), name='unique_target_device'),
        ),
    ]