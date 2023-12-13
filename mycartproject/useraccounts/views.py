from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


@login_required
def my_protected_view(request):
    return render(request, 'login.html')


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'mycartproject/home.html'


def home(request):
    if request.user.is_authenticated:
        nume_utilizator = request.user.username
        context = {'nume_utilizator': nume_utilizator}
    else:
        context = {}

    return render(request, 'home.html', context)


def login_view(request):
    return render(request, 'mycartapp/login.html')


class CustomLoginView(LoginView):
    template_name = 'useraccounts/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        if 'next' in self.request.GET:
            return redirect(self.request.GET['next'])
        else:
            return response

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('useraccounts:login')
    else:
        form = UserRegistrationForm()

    return render(request, 'useraccounts/register.html', {'form': form})
