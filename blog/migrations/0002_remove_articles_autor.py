# Generated by Django 3.1.2 on 2020-11-01 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='autor',
        ),
    ]
