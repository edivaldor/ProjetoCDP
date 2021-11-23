# Generated by Django 3.0 on 2021-11-23 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_documentospregao_declaracao_de_mepp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentospregao',
            name='contrato_social',
            field=models.FileField(blank=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='documentospregao',
            name='declaracao_de_MEPP',
            field=models.FileField(blank=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='documentospregao',
            name='declaracao_de_PARH',
            field=models.FileField(blank=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='documentospregao',
            name='procuracao_IPP',
            field=models.FileField(blank=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='documentospregao',
            name='termo_de_credenciamento',
            field=models.FileField(blank=True, upload_to='files'),
        ),
    ]
