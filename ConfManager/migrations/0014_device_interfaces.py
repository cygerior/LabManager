# Generated by Django 3.1.7 on 2021-04-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ConfManager', '0013_auto_20210404_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='interfaces',
            field=models.ManyToManyField(to='ConfManager.Interface'),
        ),
    ]