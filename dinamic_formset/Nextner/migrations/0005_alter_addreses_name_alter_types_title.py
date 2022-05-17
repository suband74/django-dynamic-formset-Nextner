# Generated by Django 4.0.4 on 2022-05-17 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nextner', '0004_alter_products_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addreses',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='types',
            name='title',
            field=models.CharField(db_index=True, max_length=80, unique=True, verbose_name='Тип товара'),
        ),
    ]