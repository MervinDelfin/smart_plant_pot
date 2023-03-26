from cgitb import handler
from django.urls import path

from . import views

app_name = 'smart_plant_pot'
urlpatterns = [
    path('', views.index, name='index'),
    path('settings/',views.settings, name="settings"),
    path('settings/set/', views.setDefinedStates, name='setDefinedStates')
]
