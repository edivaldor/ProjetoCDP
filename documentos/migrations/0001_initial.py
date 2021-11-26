# Generated by Django 3.0 on 2021-11-25 23:07

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
                ('nome', models.CharField(blank=True, max_length=100)),
                ('cpf', models.CharField(blank=True, max_length=14)),
                ('contrato_social', models.FileField(blank=True, upload_to='files')),
                ('procuracao_IPP', models.FileField(blank=True, upload_to='files')),
                ('termo_de_credenciamento', models.FileField(blank=True, upload_to='files')),
                ('declaracao_de_PARH', models.FileField(blank=True, upload_to='files')),
                ('declaracao_de_MEPP', models.FileField(blank=True, upload_to='files')),
                ('prova_de_condicao_MEPP', models.FileField(blank=True, upload_to='files')),
                ('proposta', models.FileField(blank=True, upload_to='files')),
            ],
            options={
                'verbose_name_plural': 'Documentos Pregão',
            },
        ),
    ]
