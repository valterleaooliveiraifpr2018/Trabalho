# Generated by Django 3.1.5 on 2021-02-02 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_auto_20210201_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progressao',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.classe', verbose_name='Classe pretendida'),
        ),
        migrations.AlterField(
            model_name='progressao',
            name='data_final',
            field=models.DateField(verbose_name='Data final'),
        ),
        migrations.AlterField(
            model_name='progressao',
            name='data_inicio',
            field=models.DateField(verbose_name='Data de inicio'),
        ),
    ]
