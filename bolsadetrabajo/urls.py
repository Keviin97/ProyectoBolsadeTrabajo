from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    path('', views.listar_trabajos, name='listar_trabajos'),
    path('solicitantes/', views.listar_solicitantes, name='listar_solicitantes'),

    path('trabajos/<int:pk>/', views.detalle_trabajo, name='detalle_trabajo'),
    path('solicitantes/<int:pk>/', views.detalle_solicitante, name='detalle_solicitante'),

    path('nuevo_trabajo/', views.trabajo_nuevo, name='trabajo_nuevo'),
    path('nuevo_solicitante/', views.nuevo_solicitante, name='nuevo_solicitante'),

    path('trabajos/<int:pk>/edit/', views.editar_trabajo, name='editar_trabajo'),
    path('solicitantes/<int:pk>/edit/', views.editar_solicitante, name='editar_solicitante'),

    url(r'^solicitantes/(?P<pk>\d+)/remove/$', views.eliminar_solicitante, name='eliminar_solicitante'),
    url(r'^trabajos/(?P<pk>\d+)/remove/$', views.eliminar_trabajo, name='eliminar_trabajo'),
    ]