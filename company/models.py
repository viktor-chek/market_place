from django.db import models
from django.core.exceptions import ValidationError


class Product(models.Model):
    """Модель продукции"""
    title = models.CharField(verbose_name='Название', max_length=300)
    model = models.CharField(verbose_name='Модель', max_length=100)
    release_date = models.DateTimeField(
        verbose_name='Дата выхода на рынок',
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Company(models.Model):
    """Модель компании"""
    company_types = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    ]

    type_of_company = models.SmallIntegerField(
        choices=company_types, verbose_name='Звено сети'
    )
    title = models.CharField(
        verbose_name='Название', max_length=150, unique=True
    )
    email = models.EmailField(verbose_name='Email', unique=True)

    country = models.CharField(verbose_name='Страна', max_length=100)

    city = models.CharField(verbose_name='Город', max_length=100)

    street = models.CharField(verbose_name='Улица', max_length=300)

    number_house = models.CharField(verbose_name='Номер дома', max_length=20)

    products = models.ManyToManyField(
        Product,
        verbose_name='Продукты',
        related_name='Companies',
        blank=True
    )
    supplier = models.ForeignKey(
        'company.Company',
        on_delete=models.SET_NULL,
        verbose_name='Поставщик',
        related_name='vendors',
        null=True,
        blank=True
    )

    def clean(self):
        """
        Доп проверка на запрет возможности выбирать самого себя в поставщики
        """
        if self.supplier:
            if self.supplier.id == self.id:
                raise ValidationError(
                    "Недопустимое значение"
                )

    debt = models.DecimalField(
        max_digits=30, decimal_places=2,
        verbose_name='Задолженность перед поставщиком',
        default=0)
    date_of_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
