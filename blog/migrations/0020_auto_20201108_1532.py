# Generated by Django 3.1.2 on 2020-11-08 14:32

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20201108_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actualites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contenu', tinymce.models.HTMLField()),
            ],
            options={
                'verbose_name': 'Actualités',
                'verbose_name_plural': 'Actualités',
            },
        ),
        migrations.AlterModelOptions(
            name='postimage',
            options={'verbose_name': 'Article à ne pas toucher !', 'verbose_name_plural': 'Article à ne pas toucher !'},
        ),
    ]