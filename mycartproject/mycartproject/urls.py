from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from mycartapp.views import home

urlpatterns = [
    path('', LoginView.as_view(template_name='useraccounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('mycart/', include('mycartapp.urls')),
    path('useraccounts/', include(('useraccounts.urls', 'useraccounts'), namespace='useraccounts')),
    path('home/', home, name='home'),
]
