from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.shortcuts import redirect
from django.views import generic

from .models import Tools

class IndexView(TemplateView):
    template_name = 'tools/index.html'

class ListView(generic.ListView):
    template_name = 'tools/my_tool_list.html'
    model = Tools

class CreateView(UserPassesTestMixin,generic.CreateView):
    template_name = 'tools/create.html'
    model = Tools
    fields = ['name', 'picture', 'price']

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('tools/index.html')

    def form_valid(self, form):
        form.instance.neighbor = self.request.user
        return super().form_valid(form)



# Create your views here.
