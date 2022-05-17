# Generated by Django 4.0.4 on 2022-05-07 08:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addreses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Адрес доставки')),
            ],
            options={
                'verbose_name': 'Адрес доставки',
                'verbose_name_plural': 'Адреса доставки',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=80, verbose_name='Тип товара')),
            ],
            options={
                'verbose_name': 'Тип товара',
                'verbose_name_plural': 'Типы товаров',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование товара')),
                ('delivery_date', models.DateField(default=datetime.date.today, verbose_name='Дата доставки')),
                ('file_attachment', models.FileField(upload_to='files', verbose_name='Файл')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='address', to='Nextner.addreses', verbose_name='Адрес пункта выдачи')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comment', to='Nextner.types', verbose_name='Тип товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('title',),
            },
        ),
    ]
