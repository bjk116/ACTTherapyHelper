# Generated by Django 3.2.2 on 2021-05-07 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('thoughtlogger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thought',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
