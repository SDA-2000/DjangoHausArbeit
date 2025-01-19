from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_endp),
    path('me', views.get2_endp_crud_read),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', views.registration),
    path('accounts/profile/<str:username>', views.get2_endp_crud_read),
    path('accounts/change/<str:username>/', views.change_user_data),
    path('accounts/delete/<str:username>/', views.delete_user)
]
