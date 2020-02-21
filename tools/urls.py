from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('tool_list', views.ListView.as_view(), name='tool_list'),
    path('', views.IndexView.as_view(), name='index'),


]
