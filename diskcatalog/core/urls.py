from django.urls import path
from diskcatalog.core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
]
