# Generated by Django 4.1.7 on 2023-03-19 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0011_alter_inbox_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followrequest',
            name='Summary',
        ),
        migrations.AddField(
            model_name='followrequest',
            name='summary',
            field=models.CharField(default='', max_length=255),
        ),
    ]