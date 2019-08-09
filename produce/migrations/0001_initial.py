# Generated by Django 2.2.3 on 2019-08-09 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Upload Date')),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='ApplyForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='Upload Date')),
                ('thumbnail', models.URLField(verbose_name='Thumnail Link')),
                ('video_link', models.URLField(verbose_name='Youtube Link')),
                ('produce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produce.Produce')),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
    ]