from catalog.models import Category
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Food'},
            {'name': 'Drinks', 'description': 'Tea, coffee, milkshakes'},
            {'name': 'Snacks'},
        ]

        categories_for_create = []
        for category in category_list:
            categories_for_create.append(Category(**category))

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_for_create)
