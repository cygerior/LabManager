# Generated by Django 3.2.9 on 2021-12-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConfManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='serial_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]