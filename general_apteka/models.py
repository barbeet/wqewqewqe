from django.db import models
class ProductCatalog(models.Model):
    catalog = models.CharField(max_length=100, verbose_name='Категория')

    def __str__(self):
        return self.catalog

    class Meta:
        verbose_name = u"Каталог"
        verbose_name_plural = u"Каталог"

class ProductCategory(models.Model):
    category = models.CharField(max_length=100, verbose_name='Категория')
    catalog = models.ForeignKey(ProductCatalog, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.category

    class Meta:
        verbose_name = u"Категории"
        verbose_name_plural = u"Категории"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя товара')
    price = models.DecimalField(max_digits=10, decimal_places=2 , verbose_name='Цена')
    discount = models.DecimalField(blank=True,null=True,max_digits=10, decimal_places=2 , verbose_name='Цена со скидкой')
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    company = models.CharField(max_length=100, verbose_name='Компания/Поставщик')
    testimony = models.TextField(default='Информация отсутствует.', verbose_name='Показания')
    active_substances = models.TextField(default='Информация отсутствует.', verbose_name='Активные вещества')
    application_methods = models.TextField(default='Информация отсутствует.', verbose_name='Способ применения')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    count = models.PositiveIntegerField(verbose_name='Кол-во в упаковки')
    quantity = models.PositiveIntegerField(verbose_name='Кол-во в наличии')
    recipe = models.BooleanField(default=False, verbose_name='С рецептом ДА/НЕТ')
    thermobox = models.BooleanField(default=False, verbose_name='Термозависимость ДА/НЕТ')
    comments = models.BooleanField(default=False, verbose_name='Коментарии ДА/НЕТ')
    thumb = models.ImageField(blank=True, verbose_name='Изображение')
    sales = models.IntegerField(default=0, verbose_name='Продажи')
    watches = models.IntegerField(default=0, verbose_name='Просмотры')

    class Meta:
        verbose_name = u"Товары"
        verbose_name_plural = u"Товары"
    def __str__(self):
        return self.name

class ProductDescription(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название описания')
    course = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    text = models.TextField(verbose_name='Текст в описании')

    class Meta:
        verbose_name = u"Доп описание товара"
        verbose_name_plural = u"Доп описание товара"

    def __str__(self):
        return self.title

class BasketProduct(models.Model):
    product_id = models.CharField(max_length=100, verbose_name='ID Продукта')
    login = models.CharField(max_length=100, verbose_name='Логин')
    login_hash = models.CharField(max_length=100, verbose_name='Клиент hash')
    count = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='Кол-во')
    setting_product = models.TextField(verbose_name='Настройки')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    product_done = models.BooleanField(default=False, verbose_name='Есть в наличии')

    class Meta:
        verbose_name = u"Корзина"
        verbose_name_plural = u"Корзина"

    def __str__(self):
        return self.product_id

        
class PharmacieAddress(models.Model):
    city = models.CharField(max_length=200, verbose_name='Город')
    address = models.CharField(max_length=200, verbose_name='Адресс')

    class Meta:
        verbose_name = u"Адреса аптек"
        verbose_name_plural = u"Адреса аптек"

    def __str__(self):
        return self.city


class Reviev(models.Model):
    login = models.CharField(max_length=200, verbose_name='Логин')
    id_product = models.CharField(max_length=100, verbose_name='ID Продукта')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    heading_reviev = models.CharField(max_length=200, verbose_name='Заголовок')
    text_reviev = models.CharField(max_length=200, verbose_name='Отзыв')
    published = models.BooleanField(default=False, verbose_name='Опубликовано ДА/НЕТ')

    class Meta:
        verbose_name = u"Отзывы"
        verbose_name_plural = u"Отзывы"

    def __str__(self):
        return self.login


class Question(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.CharField(max_length=100, verbose_name='E-mail')
    text = models.TextField(verbose_name='Текст')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    class Meta:
        verbose_name = u"Вопросы"
        verbose_name_plural = u"Вопросы"

    def __str__(self):
        return self.name


class ScrollBarHome(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    img = models.ImageField(blank=True, verbose_name='Изображение')
    href_button = models.CharField(blank=True, max_length=1000, verbose_name='Ссылка кнопки')
    background_color = models.CharField(max_length=200, verbose_name='Цвет заднего фона')
    title_color = models.CharField(max_length=200, verbose_name='Цвет заголовка')
    text_color = models.CharField(max_length=200, verbose_name='Цвет текста ')
    image_background = models.ImageField(blank=True,null=True, verbose_name='Изображение занего фона НЕ обязательно')


    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Скролбар домашняя страница"

    def __str__(self):
        return self.title


class ScrollBarDiscount(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    img = models.ImageField(blank=True, verbose_name='Изображение')
    href_button = models.CharField(blank=True, max_length=1000, verbose_name='Ссылка кнопки')
    background_color = models.CharField(max_length=200, verbose_name='Цвет заднего фона')
    title_color = models.CharField(max_length=200, verbose_name='Цвет заголовка')
    text_color = models.CharField(max_length=200, verbose_name='Цвет текста ')
    image_background = models.ImageField(blank=True,null=True, verbose_name='Изображение занего фона НЕ обязательно')


    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Скролбар cтраница со скидками"

    def __str__(self):
        return self.title


class Articles(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    href = models.CharField(blank=True, max_length=1000, verbose_name='Ссылка кнопки')
    img = models.ImageField(blank=True, verbose_name='Изображение')
    watches = models.IntegerField(default=0, verbose_name='Просмотры')

    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Статьи"

    def __str__(self):
        return self.title


class BackCall(models.Model):
	fio = models.CharField(max_length=200, verbose_name='ФИО')
	phone = models.CharField(max_length=200, verbose_name='Телефон')
	comment = models.TextField(verbose_name='Комментарий')
	success = models.BooleanField(default=False, verbose_name='Обработано ДА/НЕТ')

	class Meta:
		verbose_name = u""
		verbose_name_plural = u"Заявка на обратный звонок"

	def __str__(self):
		return self.fio