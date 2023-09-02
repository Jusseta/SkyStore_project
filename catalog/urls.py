from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, kinds, flowers, flower_page
from django.conf import settings
from django.conf.urls.static import static


app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('kinds/', kinds, name='kinds'),
    path('<int:pk>/flowers/', flowers, name='flowers'),
    path('<int:pk>/flower_info/', flower_page, name='flower_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
