from django.urls import path
from . import views

app_name= 'main_app'

urlpatterns = [
    path('/forms', views.get_form, name='form'),
    path('', views.index, name='index')
]