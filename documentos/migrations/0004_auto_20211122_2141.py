# Generated by Django 3.0 on 2021-11-23 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_auto_20211122_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentospregao',
            name='cpf',
            field=models.CharField(default=1, max_length=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documentospregao',
            name='nome',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]