# Generated by Django 3.0.4 on 2020-04-08 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('influencer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencer',
            name='facebook_likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='influencer',
            name='image',
            field=models.ImageField(default=0, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='influencer',
            name='instagram_followers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='influencer',
            name='interest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='influencer.Interest'),
        ),
        migrations.AddField(
            model_name='influencer',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='influencer.Level'),
        ),
        migrations.AddField(
            model_name='influencer',
            name='twitter_followers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='influencer',
            name='youtube_subscribers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='max',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='min',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
