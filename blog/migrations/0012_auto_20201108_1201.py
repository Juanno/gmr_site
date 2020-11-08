# Generated by Django 3.1.2 on 2020-11-08 11:01

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_randoscommandement_contenu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='randoscartotheque',
            options={'verbose_name': 'Commandement du Randonneur', 'verbose_name_plural': 'Commandement du Randonneur'},
        ),
        migrations.AddField(
            model_name='randoscartotheque',
            name='contenu',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='randoscartotheque',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
