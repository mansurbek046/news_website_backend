# Generated by Django 5.0.1 on 2024-01-22 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_video_article_remove_file_article_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='uploaded_file',
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
