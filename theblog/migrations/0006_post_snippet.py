# Generated by Django 4.1.2 on 2023-01-16 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='click link above to read blog post', max_length=255),
        ),
    ]
