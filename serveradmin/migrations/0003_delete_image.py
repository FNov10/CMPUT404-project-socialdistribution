# Generated by Django 4.1.6 on 2023-02-24 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serveradmin', '0002_alter_image_uploaded_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
