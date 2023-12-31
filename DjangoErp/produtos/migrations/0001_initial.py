# Generated by Django 4.2.1 on 2023-09-05 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='CFOP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='SitTributaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=500)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('foto', models.FileField(null=True, upload_to='arquivos/')),
                ('ativo', models.BooleanField(default=True)),
                ('custo', models.FloatField(null=True)),
                ('venda', models.FloatField(null=True)),
                ('ncm', models.CharField(max_length=8)),
                ('CFOP', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produtos.cfop')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produtos.categoria')),
                ('sit_tributaria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produtos.sittributaria', verbose_name='Situação Tributária')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
