from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from mailing.models import Message, Client, MailingLogs
from django.urls import reverse_lazy


class ClientCreateView(CreateView):
    """Создание профиля клиента"""
    model = Client
    fields = ('full_name', 'email', 'message',)
    success_url = reverse_lazy('mailing:clients')


class ClientListView(ListView):
    """Страница со списком клиентов"""
    model = Client
    extra_context = {'title': 'Клиенты'}


class ClientDetailView(DetailView):
    """Страница с данными клиента"""
    model = Client


class ClientUpdateView(UpdateView):
    """Изменение клиента"""
    model = Client
    fields = ('full_name', 'email', 'message',)
    success_url = reverse_lazy('mailing:clients')


class ClientDeleteView(DeleteView):
    """Удаление клиента"""
    model = Client
    success_url = reverse_lazy('mailing:clients')


class MessageCreateView(CreateView):
    """Создание рассылки"""
    model = Message
    fields = ('theme', 'body', 'time', 'frequency', 'status',)
    success_url = reverse_lazy('mailing:mail_list')


class MessageListView(ListView):
    """Страница со списком рассылок"""
    model = Message
    extra_context = {'title': 'Рассылки'}


class MessageDeleteView(DeleteView):
    """Удаление рассылки"""
    model = Message
    success_url = reverse_lazy('mailing:mail_list')


class MailingLogsListView(ListView):
    """Просмотр попыток рассылок"""
    model = MailingLogs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Попытки рассылки"
        context['log_list'] = MailingLogs.objects.all()
        return context
