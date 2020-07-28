# Generated by Django 3.1.7 on 2021-04-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ConfManager', '0014_device_interfaces'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardTypeDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='boardtype',
            name='devices',
            field=models.ManyToManyField(to='ConfManager.BoardTypeDevice'),
        ),
    ]