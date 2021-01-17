from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import Post

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

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = '__all__'  ##aqui eu defino os campos de acordo com a model


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = {'titulo', 'conteudo'}
