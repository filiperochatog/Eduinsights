# Generated by Django 5.0 on 2024-05-11 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersubmission',
            old_name='year',
            new_name='ano',
        ),
        migrations.RemoveField(
            model_name='usersubmission',
            name='cpf',
        ),
        migrations.AddField(
            model_name='usersubmission',
            name='enunciado',
            field=models.TextField(default=2008),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersubmission',
            name='numero',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
