from .views import register_user, login_view, HomeView
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='useraccounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register_user, name='register'),
    path('', login_view, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', HomeView.as_view(), name='home'),

]

