# Generated by Django 3.0 on 2021-11-22 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentosPregao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrato_social', models.FileField(blank=True, upload_to='documentos')),
                ('procuracao_IPP', models.FileField(blank=True, upload_to='documentos')),
                ('termo_de_credenciamento', models.FileField(blank=True, upload_to='documentos')),
                ('declaracao_de_PARH', models.FileField(blank=True, upload_to='documentos')),
            ],
            options={
                'verbose_name_plural': 'Documentos Pregão',
            },
        ),
    ]