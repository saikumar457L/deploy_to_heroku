from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse

from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"

class AddPost(CreateView):
    model = Post
    template_name = "blog/newpost.html"
    fields = "__all__"

class EditPost(UpdateView):
    model = Post
    template_name = "blog/editpost.html"
    fields = ["title","body"]

class DeletePost(DeleteView):
    model = Post
    template_name = "blog/deletepost.html"
    success_url = reverse_lazy("blog:home")
