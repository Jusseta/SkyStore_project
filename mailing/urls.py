from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import ClientCreateView, ClientListView, ClientDetailView, MessageCreateView


app_name = MailingConfig.name

urlpatterns = [
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients/detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('create_mail/', MessageCreateView.as_view(), name='create_mail'),
]