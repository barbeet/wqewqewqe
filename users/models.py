from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (('status_1', u'В процессе'), ('status_2', u'Ожидает'), ('status_3', u'Выполнено'), ('line_width', u'______________________________________________________________________'))
STATUS_CHOICES_QR = (('status_1', u'Ожидает'), ('status_2', u'Одобренно'), ('status_3', u'Отказано'), ('status_4', u'Использовано'))


class Profile(User):
    class Meta:
        verbose_name = u"Аккаунты"
        verbose_name_plural = u"Аккаунты"

    def __str__(self):
        return self.patronymic


class CreateNewOrder(models.Model):
    user = models.CharField(max_length=100, verbose_name='Логин')
    fio = models.CharField(blank=True,max_length=150, verbose_name='Ф.И.О')
    all_product_id_and_count = models.CharField(max_length=1000, verbose_name='Список товаров')
    all_product_id_and_count_dict = models.CharField(max_length=1000, verbose_name='Список товаров dict')
    sum_all = models.FloatField(verbose_name='Общая цена')
    method_of_obtaining = models.CharField(max_length=100, verbose_name='Метод доставки')
    payment_method = models.CharField(max_length=100, verbose_name='Метод оплаты')
    contact = models.CharField(max_length=100, verbose_name='Контакты')
    address = models.CharField(max_length=150, verbose_name='Адресс аптеки')
    date_add_order = models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления')
    status = models.CharField(max_length=200,choices=STATUS_CHOICES, verbose_name='Статус')

    class Meta:
        verbose_name = u"Заказы"
        verbose_name_plural = u"Заказы"

    def __str__(self):
        return self.user


class QrCodeSave(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='Имя продукта')
    id_product = models.CharField(max_length=200, verbose_name='ID продукта')
    count = models.PositiveIntegerField(verbose_name='Кол-во продукта')
    user = models.CharField(max_length=100, verbose_name='Логин')
    image = models.ImageField(verbose_name='QR image')
    qr_value = models.CharField(max_length=1000,verbose_name='Значение QR')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    comment = models.TextField(blank=True,null=True, verbose_name='Коментарий')
    status = models.CharField(max_length=200,choices=STATUS_CHOICES_QR, verbose_name='Статус')

    class Meta:
        verbose_name = u"QR code"
        verbose_name_plural = u"QR code"

    def __str__(self):
        return self.product_name


class PriceDelivery(models.Model):
    name = models.CharField(max_length=200, verbose_name='Доставка')
    add_price = models.PositiveIntegerField(verbose_name='Плюс к стоимости')
    min_sum_price_order = models.PositiveIntegerField(verbose_name='Минимальная сумма заказа')
    class Meta:
        verbose_name = u"Цены за доставку"
        verbose_name_plural = u"Цены за доставку"

    def __str__(self):
        return self.name