# Generated by Django 3.1.5 on 2021-02-08 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20210206_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='nome_completo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefone',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
