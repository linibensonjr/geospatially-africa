# Generated by Django 3.2.6 on 2021-08-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('desc', models.TextField()),
            ],
        ),
    ]
