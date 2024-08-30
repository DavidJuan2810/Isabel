from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListarVestido, name= 'ListarVestido'),
    path('crear/',views.registrarVestido, name='registrarVestido')
]