from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('my_tool_list', views.ListView.as_view(), name='my_tool_list'),
    path('my_tool_list/create/', views.CreateView.as_view(), name='create'),
    path('', views.IndexView.as_view(), name='index'),


]
