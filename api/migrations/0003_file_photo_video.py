# Generated by Django 5.0.1 on 2024-01-21 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='api.article')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='api.article')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='api.article')),
            ],
        ),
    ]
