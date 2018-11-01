from django.urls import include, path
from . import views

app_name = 'software'

urlpatterns = [
    path('', views.index, name='index'),
    path('softwaredepartamento/<str:name>/', views.index_filter, name='index_filter'),
    path('detalles/<int:id>/', views.detalles, name='detalles'),
    path('alta_software/', views.alta_software, name='alta_software'),
    path('alta_departamento/', views.alta_departamento, name='alta_departamento'),

]