from django.views.generic.base import TemplateView
from django.views import generic

from .models import Tools

class IndexView(TemplateView):
    template_name = 'tools/index.html'

class ListView(generic.ListView):
    template_name = 'tools/my_tool_list.html'
    model = Tools

# Create your views here.
