from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('tools/user/<int:pk>/delete', views.ToolDeleteView.as_view(), name='delete_tool'),
    path('tools/user/<int:pk>/edit', views.ToolUpdateView.as_view(), name='edit_tool'),
    path('tools/all/', views.ListView.as_view(), name='tool_list'),
    path('tools/user/<int:pk>/', views.ListView.as_view(), name='user_tool_list'),
    path('tools/create/', views.CreateView.as_view(), name='tool_create'),
    path('', views.IndexView.as_view(), name='index'),
]
