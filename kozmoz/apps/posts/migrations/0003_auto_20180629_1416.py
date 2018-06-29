# Generated by Django 2.0.6 on 2018-06-29 14:16

import datetime
from django.db import migrations, models
import posts.formatChecker


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publishing_date',
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 6, 29, 14, 16, 53, 717506), verbose_name='Published_Date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='media',
            field=posts.formatChecker.ContentTypeRestrictedFileField(upload_to='media/video'),
        ),
    ]