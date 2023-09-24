from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='vikki0011@gmail.com',
            first_name='Victoria',
            last_name='Kashpur',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('1234qwer')
        user.save()
