# Generated by Django 2.2.3 on 2019-08-07 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0007_auto_20190727_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-upload_date']},
        ),
    ]
