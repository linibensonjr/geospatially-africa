# Generated by Django 3.2.6 on 2022-10-13 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='cohost',
            field=models.CharField(blank=True, choices=[('Iniobong Benson', 'Iniobong'), ('Opeyemi Kazeem-Jimoh', 'Opeyemi')], max_length=500, null=True),
        ),
    ]
