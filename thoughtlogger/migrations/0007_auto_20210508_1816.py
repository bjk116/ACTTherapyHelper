# Generated by Django 3.2.2 on 2021-05-08 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thoughtlogger', '0006_auto_20210508_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SelectedValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importance', models.TextField()),
                ('routines', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='thoughtlogger.routines')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='thoughtlogger.value')),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milestone_text', models.CharField(max_length=300)),
                ('complete_date', models.DateTimeField(null=True)),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='thoughtlogger.value')),
            ],
        ),
        migrations.AddField(
            model_name='routines',
            name='milestone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='thoughtlogger.milestone'),
        ),
    ]
