# Generated by Django 2.2.3 on 2019-07-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_photo_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='video_link',
            field=models.URLField(null=True),
        ),
    ]