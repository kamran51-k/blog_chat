# Generated by Django 4.0 on 2021-12-12 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogchat_app', '0006_postmodel_pp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='pp',
        ),
    ]
