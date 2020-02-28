from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views import generic

from .models import Tool

class IndexView(TemplateView):
    template_name = 'tools/index.html'

class ListView(generic.ListView):
    template_name = 'tools/tool_list.html'
    model = Tool

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Tool.objects.filter(neighbor = self.request.user)
        return Tool.objects.all()


class CreateView(LoginRequiredMixin,generic.CreateView):
    template_name = 'tools/create.html'
    model = Tool
    fields = ['name', 'picture', 'price']

    def test_func(self):
        return self.request.user.is_superuser

#if user doens't have permission it will redirect to this page
    def handle_no_permission(self):
        return redirect('tools/index.html')

    def form_valid(self, form):
        form.instance.neighbor = self.request.user
        return super().form_valid(form)

class ToolUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = Tool
    template_name = 'tools/edit.html'
    fields = ['name', 'picture', 'price']

    def test_func(self):
        obj = self.get_object()
        return obj.neighbor == self.request.user

#if user doens't have permission it will redirect to this page
    def handle_no_permission(self):
        return redirect('tools:tool_list')


class ToolDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = Tool
    success_url = reverse_lazy('tools:tool_list')

    def test_func(self):
        obj = self.get_object()
        return obj.neighbor == self.request.user

    def handle_no_permission(self):
        return redirect('tools:tool_list')




# Create your views here.
