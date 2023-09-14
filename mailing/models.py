from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(max_length=150, verbose_name='Почта')
    message = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.full_name} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
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
    time = models.TimeField(auto_now_add=True, verbose_name='Время рассылки', **NULLABLE)
    frequency = models.CharField(choices=frequency_list, verbose_name='Периодичность', **NULLABLE)
    status = models.CharField(choices=status_list, verbose_name='Статус', **NULLABLE)

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingLogs(models.Model):
    status_list = [
        ('Success', 'успешно'),
        ('Failure', 'отказ')
    ]

    last_try = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки')
    status = models.CharField(max_length=100, choices=status_list, verbose_name='Статус попытки')
    server_response = models.TextField(verbose_name='Ответ почтового сервера', **NULLABLE)

    def __str__(self):
        return f'Последняя попытка была {self.last_try}, статус "{self.status}"'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
