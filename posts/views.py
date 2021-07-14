from django.shortcuts import render
from .models import Post, Profile, User
from django.views.generic import ListView,CreateView,DetailView,UpdateView
from .models  import Post
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
def hendler404(request,exception):
       return render(request,'a/404.html',status=404)

class News(LoginRequiredMixin,CreateView):
    model=Post
    fields=('text',)
    template_name='new.html'
    pk_url_kwarg = "post_id"
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


def user_posts(request, username):
  posts = Post.objects.filter(author__username=username)
  return render(request, 'profile.html', {'posts':posts})

    
def post_view(request,username,post_id):
    post = Post.objects.get(id=post_id) 
    posts = Post.objects.filter(author__username=username)
    context={'post':post, 'posts':posts}
    return render(request, 'post.html',context)
# Create your views here.

class Update(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['text']
    success_url=reverse_lazy('index')
    pk_url_kwarg = "post_id"
    def test_func(self): 
        obj=self.get_object()
        return obj.author==self.request.user
    
    


