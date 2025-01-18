from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_endp),
    path('me', views.get2_endp),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', views.registration),
    path('accounts/profile/', views.get2_endp)
]
