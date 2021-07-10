from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,CreateView
from .models  import Post
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class New(LoginRequiredMixin,CreateView):
    model=Post
    fields=['text']
    template_name='new.html'
    success_url=reverse_lazy('index')
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostList(LoginRequiredMixin,ListView):
    model=Post
    context_object_name='posts'
    paginate_by=6

    
    ordering=['-pub_date']
    template_name='index.html'




# Create your views here.
