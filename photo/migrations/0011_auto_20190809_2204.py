# Generated by Django 2.2.3 on 2019-08-09 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0010_auto_20190807_2015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-upload_date']},
        ),
    ]
