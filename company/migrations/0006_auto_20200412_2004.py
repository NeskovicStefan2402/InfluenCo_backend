# Generated by Django 3.0.4 on 2020-04-12 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('influencer', '0007_auto_20200412_1936'),
        ('company', '0005_auto_20200412_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='selected',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='influencer.Influencer'),
        ),
    ]