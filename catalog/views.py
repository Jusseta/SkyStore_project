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
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'object': product_item,
        'title': product_item.name,
        'description': f'Описание сорта: {product_item.description}',
        'category': f'Относится к виду {product_item.category}',
        'price': product_item.price,
        'created_at': f'Дата создания {product_item.created_at}'
    }
    return render(request, 'catalog/flower_page.html', context)
