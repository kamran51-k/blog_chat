# Generated by Django 4.0 on 2021-12-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogchat_app', '0012_remove_comment_email_comment_reply_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='category',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='semester',
            field=models.CharField(choices=[('Personal Post', 'Personal Post'), ('Visual Designs', 'Visual Designs'), ('Travel Events', 'Travel Events'), ('Web Development', 'Web Development'), ('Video and Audio', 'Video and Audio')], default='Personal Post', max_length=20),
        ),
    ]
