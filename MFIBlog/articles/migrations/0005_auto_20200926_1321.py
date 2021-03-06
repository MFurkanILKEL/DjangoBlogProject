# Generated by Django 3.1 on 2020-09-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200926_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forensic',
            name='title',
            field=models.CharField(max_length=60, unique=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='network',
            name='title',
            field=models.CharField(max_length=60, unique=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='security',
            name='title',
            field=models.CharField(max_length=60, unique=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='tools',
            name='title',
            field=models.CharField(max_length=60, unique=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='translate',
            name='summary',
            field=models.CharField(max_length=90, unique=True, verbose_name='Açıklama'),
        ),
    ]
