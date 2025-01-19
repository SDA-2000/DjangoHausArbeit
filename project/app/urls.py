from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.red),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
