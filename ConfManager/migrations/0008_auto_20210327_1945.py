# Generated by Django 3.1.3 on 2021-03-27 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ConfManager', '0007_auto_20210327_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='powersupply',
            options={'ordering': ['port_number'], 'verbose_name_plural': 'Power supplies'},
        ),
        migrations.RemoveField(
            model_name='powersupply',
            name='name',
        ),
        migrations.AlterField(
            model_name='rackslot',
            name='board',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ConfManager.board'),
        ),
        migrations.AddConstraint(
            model_name='powersupply',
            constraint=models.UniqueConstraint(fields=('port_number', 'controller'), name='unique_port_controller'),
        ),
        migrations.AddField(
            model_name='resource',
            name='labels',
            field=models.ManyToManyField(to='ConfManager.Label'),
        ),
    ]
