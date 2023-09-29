from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import CreateView
from users.forms import UserRegisterForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.is_active = False
            self.object.token = get_random_string(length=15)
            self.object.save()
            send_mail(
                subject='Верификация пользователя',
                message=f'Для завершения регистрации пройдите по ссылке http://127.0.0.1:8000/users/verify_{self.object.token}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email]
            )
            return super().form_valid(form)


def verify(request, key):
    user_item = get_object_or_404(User, token=key)
    user_item.is_active = True
    user_item.save(update_fields=['is_active'])
    return render(request, 'users/verify_message.html')
