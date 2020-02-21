from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('my_tool_list', views.ListView.as_view(), name='my_tool_list'),
    path('', views.IndexView.as_view(), name='index'),


]
