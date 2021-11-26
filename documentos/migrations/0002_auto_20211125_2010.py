# Generated by Django 3.0 on 2021-11-25 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentospregao',
            name='contrato_social',
            field=models.FileField(blank=True, upload_to='documentos'),
        ),
        migrations.AlterField(
            model_name='documentospregao',
            name='declaracao_de_MEPP',
            field=models.FileField(blank=True, upload_to='documentos'),
        ),
        migrations.AlterField(
            model_name='documentospregao',
            name='declaracao_de_PARH',
            field=models.FileField(blank=True, upload_to='documentos'),
        ),
        migrations.AlterField(
            model_name='documentospregao',
            name='procuracao_IPP',
            field=models.FileField(blank=True, upload_to='documentos'),
        ),
        migrations.AlterField(
            model_name='documentospregao',
            name='proposta',
            field=models.FileField(blank=True, upload_to='documentos'),
        ),
        migrations.AlterField(
            model_name='documentospregao',
            name='prova_de_condicao_MEPP',
            field=models.FileField(blank=True, upload_to='documentos'),
        ),
        migrations.AlterField(
            model_name='documentospregao',
            name='termo_de_credenciamento',
            field=models.FileField(blank=True, upload_to='documentos'),
        ),
    ]