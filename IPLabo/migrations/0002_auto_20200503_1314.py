# Generated by Django 3.0.5 on 2020-05-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('IPLabo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ippool',
            name='ip',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
