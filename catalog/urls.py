from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, contacts, CategoryListView, ProductListView, ProductsDetailView, BlogListView, \
    BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.conf import settings
from django.conf.urls.static import static


app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('flowers/<int:pk>/', ProductListView.as_view(), name='flowers'),
    path('flower_detail/<int:pk>/', ProductsDetailView.as_view(), name='flower_detail'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('add_blog/', BlogCreateView.as_view(), name='add_blog'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
