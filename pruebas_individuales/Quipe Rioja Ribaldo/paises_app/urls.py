from django.urls import path
from . import views

urlpatterns = [
    path('',                    views.lista_paises,    name='lista_paises'),
    path('nuevo/',              views.crear_pais,      name='crear_pais'),
    path('<int:pk>/',           views.detalle_pais,    name='detalle_pais'),
    path('<int:pk>/editar/',    views.editar_pais,     name='editar_pais'),
    path('<int:pk>/eliminar/',  views.eliminar_pais,   name='eliminar_pais'),
    path('valor/<int:pk>/eliminar/', views.eliminar_valor, name='eliminar_valor'),
]
