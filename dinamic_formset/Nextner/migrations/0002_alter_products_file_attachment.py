# Generated by Django 4.0.4 on 2022-05-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nextner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='file_attachment',
            field=models.FileField(upload_to='media', verbose_name='Файл'),
        ),
    ]
