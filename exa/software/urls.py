from django.urls import include, path
from . import views

app_name = 'software'

urlpatterns = [
    path('', views.index, name='index'),
    path('CIENCIAS COMPUTACIONALES/', views.cat01, name='cat01'),
    path('CIENCIAS DE LA TIERRA/', views.cat02, name='cat02'),
    path('CIENCIAS NATURALES/', views.cat03, name='cat03'),
    path('CIENCIAS SOCIALES/', views.cat04, name='cat04'),
    path('CIENCIAS MEDICAS/', views.cat05, name='cat05'),
    path('details/<int:id>/', views.details, name='details'),
    path('create/', views.create, name='create'),
]