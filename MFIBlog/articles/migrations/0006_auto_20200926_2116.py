# Generated by Django 3.1 on 2020-09-26 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200926_1321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forensic',
            options={'ordering': ['-createDate']},
        ),
        migrations.AlterModelOptions(
            name='network',
            options={'ordering': ['-createDate']},
        ),
        migrations.AlterModelOptions(
            name='security',
            options={'ordering': ['-createDate']},
        ),
        migrations.AlterModelOptions(
            name='tools',
            options={'ordering': ['-createDate']},
        ),
        migrations.AlterModelOptions(
            name='translate',
            options={'ordering': ['-createDate']},
        ),
    ]
