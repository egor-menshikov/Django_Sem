# Generated by Django 5.0.4 on 2024-04-20 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=100)),
                ('views', models.BigIntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.author')),
            ],
        ),
    ]
