# Generated by Django 3.2.6 on 2022-10-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0002_episode_cohost'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='applepodcast',
            field=models.CharField(default='https://podcasts.apple.com/us/podcast/geospatially-africa-podcast-the-podcast-for/id1561204113', help_text='Provide link to episode on Apple Podcasts', max_length=1500),
        ),
        migrations.AddField(
            model_name='episode',
            name='googlepodcast',
            field=models.CharField(default='https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy80ZDg4MWJhMC9wb2RjYXN0L3Jzcw?sa=X&ved=2ahUKEwjFxoL134D7AhUugc4BHXz1BeQQ9sEGegQIARAC', help_text='Provide link to episode on Google Podcasts', max_length=1500),
        ),
        migrations.AddField(
            model_name='episode',
            name='spotify',
            field=models.CharField(default='https://open.spotify.com/show/7aqyurtRoF42hTysOqNa9v?si=9779d6cefca74f82', help_text='Provide link to episode on Spotify', max_length=1500),
        ),
        migrations.AlterField(
            model_name='episode',
            name='link',
            field=models.CharField(help_text='Provide embed link to episode audio', max_length=1500),
        ),
    ]
