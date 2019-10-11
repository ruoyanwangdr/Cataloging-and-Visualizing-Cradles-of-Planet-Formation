from django.urls import path
from . import views

urlpatterns = [
    # /disk/
    path('', views.index, name='index'),

    # /disk/<int:id>/
    path('<int:resolved_id>/', views.detail, name='detail'),
]
