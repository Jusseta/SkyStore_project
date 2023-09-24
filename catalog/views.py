from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from pytils.translit import slugify
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Blog, Version


class HomeView(TemplateView):
    """Домашняя страница"""
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()[:3]
        return context_data


def contacts(request):
    """Страница контактов"""
    return render(request, 'catalog/contacts.html')


class CategoryListView(ListView):
    """Страница со списком категорий"""
    model = Category
    extra_context = {'title': 'Все виды цветов'}


class ProductListView(ListView):
    """Страница со списком продуктов по категориям"""
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Цветы сорта {category_item.name}'
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:categories')
    extra_context = {'heading': 'Добавить цветок'}


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    extra_context = {'heading': 'Изменить цветок'}

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:flower_detail', args=(self.object.id,))


class ProductsDetailView(DetailView):
    """Страница продукта"""
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


class BlogListView(ListView):
    """Страница со списком статей блога"""
    model = Blog
    extra_context = {'title': 'Блог'}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_products = Product.objects.all()
        context['all_product_list'] = all_products
        return context


class BlogDetailView(DetailView):
    """Страница статьи"""
    model = Blog

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    """Создание новой статьи"""
    model = Blog
    fields = ('title', 'content', 'is_published',)
    success_url = reverse_lazy('catalog:blogs')
    extra_context = {'heading': 'Создание статьи'}

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """Изменение существующей статьи"""
    model = Blog
    fields = ('title', 'content', 'is_published',)
    extra_context = {'heading': 'Изменение статьи'}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        context['title'] = context['object']
        return context

    def get_success_url(self):
        return reverse_lazy('catalog:blog_detail', args=(self.object.id,))


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление статьи"""
    model = Blog
    success_url = reverse_lazy('catalog:blogs')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_products = Product.objects.all()
        context['all_product_list'] = all_products
        context['title'] = context['object']
        return context
