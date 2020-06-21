from django.urls import path
#importo vistas desde root para tener aceso a las vistas
from . import views 
'''
este urls es creado por mi, lo primero que hago es definir los patrones
de la url como una lista vacia y a partir de ahi la iremos llenando con
las rutas nuevas de l app
'''
urlpatterns = [
    path('', views.index, name = "mainlist"),
    path('edit_task/<str:pk>/', views.editTask, name = "edit_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name = "delete_task")
]