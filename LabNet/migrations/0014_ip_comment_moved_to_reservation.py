# Generated by Django 3.2.5 on 2021-07-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LabNet', '0013_ip_ip_to_interger_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ip',
            name='comment',
        ),
        migrations.AddField(
            model_name='reservation',
            name='comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
