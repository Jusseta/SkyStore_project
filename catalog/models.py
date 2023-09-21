from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """Модель категории"""
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=300, **NULLABLE, verbose_name='Описание')
    created_at = models.DateField(max_length=50, **NULLABLE, verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=300, **NULLABLE, verbose_name='Описание')
    preview = models.ImageField(upload_to='images/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(default=0, verbose_name='Цена за покупку')
    created_at = models.DateField(max_length=50, **NULLABLE, verbose_name='Дата создания', auto_now_add=True)
    last_changes = models.DateField(max_length=50, **NULLABLE, verbose_name='Дата последнего изменения', auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Blog(models.Model):
    """Модель блога"""
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.CharField(max_length=200, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Cодержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class Version(models.Model):
    """Версия продукта"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.TextField(max_length=50, verbose_name='Номер версии')
    version_name = models.TextField(max_length=200,verbose_name='Название версии')
    version_flag = models.BooleanField(verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.product}, {self.version_number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
