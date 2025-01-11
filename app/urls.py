from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # path('', views.hola_mundo, name='hola_mundo'),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', views.login_view, name='login'),  # Usa la vista personalizada

    # path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', views.logout_view, name='logout'),

    path('register/', views.register, name='register'),
    path('welcome/<int:user_id>/', views.welcome, name='welcome'),  # Cambia a `int:user_id`


]  