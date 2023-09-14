from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from mailing.models import Message, Client
from django.urls import reverse_lazy


class ClientCreateView(CreateView):
    model = Client
    fields = ('full_name', 'email', 'message',)
    success_url = reverse_lazy('catalog:blogs')


class ClientListView(ListView):
    model = Client
    extra_context = {'title': 'Клиенты'}

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class ClientDetailView(DetailView):
    model = Client


class MessageCreateView(CreateView):
    model = Message
    fields = ('theme', 'body', 'time', 'frequency', 'status',)
    success_url = reverse_lazy('catalog:blogs')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
