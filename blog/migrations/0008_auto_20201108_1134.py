# Generated by Django 3.1.2 on 2020-11-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_detailsejour_manifestation_photosarticles_randosanimateur_randoscalendrier_randoscartotheque_randosc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='randoscalendrier',
            options={'verbose_name': 'Calendrier Semestriel', 'verbose_name_plural': 'Calendrier Semestriel'},
        ),
        migrations.AlterModelOptions(
            name='randoscommandement',
            options={'verbose_name': 'Commandement du Randonneur', 'verbose_name_plural': 'Commandement du Randonneur'},
        ),
        migrations.AddField(
            model_name='randoscalendrier',
            name='calendrier_pdf',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='randoscalendrier',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
