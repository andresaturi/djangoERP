# Generated by Django 4.2.1 on 2023-08-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=150)),
                ('recebido', models.BooleanField(default=False)),
                ('pessoa', models.CharField(max_length=100)),
            ],
        ),
    ]
