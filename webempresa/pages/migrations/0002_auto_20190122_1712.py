# Generated by Django 2.1.4 on 2019-01-22 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'ordering': ['order', '-title'], 'verbose_name': 'Página', 'verbose_name_plural': 'Páginas'},
        ),
        migrations.AddField(
            model_name='pages',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='orden'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='content',
            field=models.TextField(verbose_name='contenido'),
        ),
    ]
