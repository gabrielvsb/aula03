# Generated by Django 2.2.1 on 2019-08-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0002_auto_20190830_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticia',
            options={'verbose_name': 'Noticia', 'verbose_name_plural': 'Noticias'},
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=128, verbose_name='titulo'),
        ),
    ]