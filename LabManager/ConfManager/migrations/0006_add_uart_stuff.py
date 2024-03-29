# Generated by Django 3.2.5 on 2022-09-11 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ConfManager', '0005_order_power_supplies'),
    ]

    operations = [
        migrations.CreateModel(
            name='UartGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UartServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('url', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UartPort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfManager.uartserver')),
            ],
        ),
        migrations.CreateModel(
            name='UartGroupEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uart_number', models.IntegerField()),
                ('uart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ConfManager.uartport')),
                ('uart_connector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfManager.uartgroup')),
            ],
            options={
                'verbose_name_plural': 'Uart group entries',
                'ordering': ['uart_number'],
            },
        ),
        migrations.AddField(
            model_name='uartgroup',
            name='uart_ports',
            field=models.ManyToManyField(through='ConfManager.UartGroupEntry', to='ConfManager.UartPort'),
        ),
        migrations.AddConstraint(
            model_name='uartgroupentry',
            constraint=models.UniqueConstraint(fields=('uart_number', 'uart_connector'), name='unique_group_uart_number'),
        ),
    ]
