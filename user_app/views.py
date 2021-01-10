from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from django.views import View

from user_app.form import UserRegisterForm, UserLogin
from user_app.models import ChangerUser


class RegisterUser(View):
    form_class = UserRegisterForm
    initial = {}
    template_name = ''

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form', form})


class UserRegister(generic.CreateView):
    template_name = 'static/login'
    model = ChangerUser
    form_class = UserRegisterForm
    success_url = reverse_lazy('')


class UserLoginView(generic.FormView):
    template_name = 'static/login.html'
    form_class = UserLogin
    success_url = ''

    def form_valid(self, form):
        username = form.instance.username
        password = form.instance.password
        login(username, password)