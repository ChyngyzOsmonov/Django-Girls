from django.shortcuts import render
from .models import ToDoList
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy


class DoList(ListView):
    model = ToDoList
    template_name = 'do_list.html'
    # fields = ['status']


class CreateList(CreateView):
    model = ToDoList
    template_name = 'create.html'
    fields = ['title']
    success_url = reverse_lazy('list')


class UpdateList(UpdateView):
    model = ToDoList
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('list')


class DeleteList(DeleteView):
    model = ToDoList
    template_name = 'delete.html'
    success_url = reverse_lazy('list')



