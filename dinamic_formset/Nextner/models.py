from django.db import models

from datetime import date


class Types(models.Model):
    title = models.CharField("Тип товара", max_length=80, db_index=True, unique=True)

    class Meta:
        verbose_name = "Тип товара"
        verbose_name_plural = "Типы товаров"

    def __str__(self) -> str:
        return self.title


class Addreses(models.Model):
    name = models.CharField("Адрес доставки", max_length=255, unique=True)

    class Meta:
        verbose_name = "Адрес доставки"
        verbose_name_plural = "Адреса доставки"

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    title = models.CharField("Наименование товара", max_length=255)
    product_type = models.ForeignKey(
        Types,
        on_delete=models.PROTECT,
        verbose_name="Тип товара",
    )

    delivery_date = models.DateField("Дата доставки", default=date.today)

    file_attachment = models.FileField("Файл", upload_to="media")
    address = models.ForeignKey(
        Addreses,
        on_delete=models.PROTECT,
        verbose_name="Адрес пункта выдачи",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("delivery_date", "title")

    def __str__(self) -> str:
        return f"{self.title} на {self.address}, {self.delivery_date}"
