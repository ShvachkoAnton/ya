from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Post,Contact
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from .forms import CommentForm
from django.views.generic import ListView,CreateView,DetailView,UpdateView
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import JsonResponse,HttpResponseRedirect
from django.views.decorators.http import require_POST
from common.decorators import ajax_required

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
def hendler404(request,exception):
       return render(request,'a/404.html',status=404)

class News(LoginRequiredMixin,CreateView):
    model=Post
    fields=('text','image')
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

@cache_page(60*15)
def user_posts(request, username):   #все посты
  tak=Post.objects.all
  posts = Post.objects.filter(author__username=username ) # от конкретного автора
  return render(request, 'profile.html', {'posts':posts,'tak':tak })

    
def post_view(request,username,post_id): #каждый по отдельности
    post = Post.objects.get(id=post_id) 
    posts = Post.objects.filter(author__username=username)
    context={'post':post, 'posts':posts}
    return render(request, 'post.html',context)

@login_required
def comment_add(request,username,post_id):
    post=Post.objects.get(id=post_id)
    
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            
            comment=form.save(commit=False)
            comment.author = request.user
            
            comment.post=post
            comment.save()
            return redirect('index')
    else:
        form=CommentForm()
    return render(request,'add_comments.html',{'form':form})







class Update(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['text','image']
    success_url=reverse_lazy('index')
    pk_url_kwarg = "post_id"
    def test_func(self): 
        obj=self.get_object()
        return obj.author==self.request.user
    
    



@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request,'user_list.html',{'section': 'people','users': users})
@login_required
def user_detail(request, username):
    user = get_object_or_404(User,username=username,is_active=True)
    return render(request,'user_detail.html',{'section': 'people',
    'user': user})


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user,user_to=user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'error'})
    return JsonResponse({'status':'error'})

def profile(request, username,):
    userProfile = User.objects.get(username=username)
    
    tak=Post.objects.filter(author__username=username)
    data = {
        "author": userProfile, 'tak':tak
    }
    return render(request, "authorprofile.html", data)




def followToggle(request, author):
    authorObj = User.objects.get(username=author)
    currentUserObj = User.objects.get(username=request.user.username)
    following = authorObj.following.all()

    if author != currentUserObj.username:
        if currentUserObj in following:
            authorObj.following.remove(currentUserObj.id)
        else:
            authorObj.following.add(currentUserObj.id)

    return HttpResponseRedirect(reverse(profile, args=[authorObj.username]))