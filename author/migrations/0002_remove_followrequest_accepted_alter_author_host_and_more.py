# Generated by Django 4.1.6 on 2023-04-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followrequest',
            name='accepted',
        ),
        migrations.AlterField(
            model_name='author',
            name='host',
            field=models.URLField(default='https://sociallydistributed.herokuapp.com/', editable=False, max_length=500),
        ),
        migrations.AlterField(
            model_name='node',
            name='url',
            field=models.URLField(default='https://sociallydistributed.herokuapp.com/', editable=False, max_length=500),
        ),
    ]
