# Generated by Django 3.0.4 on 2020-04-20 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencer', '0009_auto_20200420_1141'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AlterField(
            model_name='influencer',
            name='image',
            field=models.ImageField(upload_to='influencers/'),
        ),
    ]
