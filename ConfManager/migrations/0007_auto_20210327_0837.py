# Generated by Django 3.1.3 on 2021-03-27 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ConfManager', '0006_auto_20201107_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='powersupply',
            options={'verbose_name_plural': 'Power Supplies'},
        ),
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='boardtype',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='powercontroller',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='powersupply',
            name='name',
            field=models.CharField(max_length=30, unique=True, null=True),
        ),
        migrations.CreateModel(
            name='RackSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_id', models.IntegerField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfManager.board')),
                ('rack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfManager.rack')),
            ],
        ),
        migrations.AddField(
            model_name='rack',
            name='board',
            field=models.ManyToManyField(through='ConfManager.RackSlot', to='ConfManager.Board'),
        ),
    ]