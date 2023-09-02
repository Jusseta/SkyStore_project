from django.shortcuts import render
from catalog.models import Category, Product


def home(request):
    context = {
        'object_list': Category.objects.all()
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def kinds(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/kinds.html', context)


def flowers(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Цветы сорта {category_item.name}'
    }
    return render(request, 'catalog/kinds.html', context)


def flower_page(request, pk):
    context = {
        'object_list': Product.objects.filter(category_id=pk),
    }
    return render(request, 'catalog/flower_page.html', context)
