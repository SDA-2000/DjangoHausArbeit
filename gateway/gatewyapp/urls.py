from django.urls import path, include
from . import views
urlpatterns = [
    path('<path:path>', views.GateWayView.as_view())
]
