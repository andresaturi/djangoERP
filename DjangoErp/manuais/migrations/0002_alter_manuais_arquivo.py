# Generated by Django 4.2.1 on 2023-08-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuais', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manuais',
            name='arquivo',
            field=models.FileField(null=True, upload_to='arquivos/'),
        ),
    ]
