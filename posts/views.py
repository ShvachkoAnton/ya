from django.shortcuts import render
from .models import Post, Profile, User
from django.views.generic import ListView,CreateView,DetailView
from .models  import Post
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


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


def profile(request,pk=None):
       

    if pk:
            
        post_owner = get_object_or_404(User, pk=pk)
        user_posts=Post.objects.filter(author_id=pk)
            
    else:
        post_owner = request.author
        user_posts=Post.objects.filter(author_id=pk)
    return render(request, 'profile.html', {'post_owner': post_owner, 'user_posts': user_posts})

# Create your views here.
