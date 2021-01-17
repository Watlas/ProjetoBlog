from django.shortcuts import render
from django.http import HttpResponse
import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Post
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

#
#
# # Create your views here.
# def current_datetime(request):
#     data = {'data': datetime.datetime.now()}
#     return render(request, 'blog/home.html', data)
#

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'custom'

class BlogCreateView(SuccessMessageMixin,CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields =  {'autor', 'titulo', 'conteudo'}   #'__all__'  ##aqui eu defino os campos de acordo com a mod
    success_message = "%(field)s Criado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )

class BlogUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = {'titulo', 'conteudo'}
    success_message = "%(field)s Alterado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )

class BlogDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)