# Generated by Django 3.0 on 2021-11-23 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0005_auto_20211122_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentospregao',
            name='contrato_social',
            field=models.ImageField(blank=True, upload_to='files'),
        ),
    ]
