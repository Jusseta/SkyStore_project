from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import *


app_name = MailingConfig.name

urlpatterns = [
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('create_mail/', MessageCreateView.as_view(), name='create_mail'),
    path('mail_list/', MessageListView.as_view(), name='mail_list'),
    path('mail_delete/<int:pk>/', MessageDeleteView.as_view(), name='mail_delete'),
    path('mail_logs/', MailingLogsListView.as_view(), name='mail_logs'),
]
