# Generated by Django 3.1.2 on 2020-11-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_accueil'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accueil',
            options={'verbose_name': 'Accueil', 'verbose_name_plural': 'Accueil'},
        ),
        migrations.AddField(
            model_name='accueil',
            name='image',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
