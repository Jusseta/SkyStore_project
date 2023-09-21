from datetime import datetime

from django.db import models
from django.utils import timezone


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Модель клиента"""
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(max_length=150, verbose_name='Почта')
    message = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.full_name} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    """Модель сообщения для рассылки"""
    frequency_list = [
        ('day', 'раз в день'),
        ('week', 'раз в неделю'),
        ('month', 'раз в месяц')
    ]

    status_list = [
        ('finish', 'завершена'),
        ('create', 'создана'),
        ('start', 'запущена')
    ]

    theme = models.CharField(max_length=100, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')
    time = models.DateTimeField(default=datetime.now, verbose_name='Время рассылки')
    frequency = models.CharField(choices=frequency_list, default='day', verbose_name='Периодичность')
    status = models.CharField(choices=status_list, default='create', verbose_name='Статус')

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingLogs(models.Model):
    """Модель логов рассылки"""
    status_list = [
        ('success', 'успешно'),
        ('failure', 'отказ')
    ]

    last_try = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки')
    status = models.CharField(max_length=100, choices=status_list, verbose_name='Статус попытки')
    server_response = models.TextField(verbose_name='Ответ почтового сервера', **NULLABLE)

    def __str__(self):
        return f'Последняя попытка была {self.last_try}, статус "{self.status}"'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
