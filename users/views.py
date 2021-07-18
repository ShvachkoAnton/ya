from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm, Name

from django.urls import reverse_lazy

from django.views.decorators.cache import cache_page

class SignUpp(CreateView):
    form_class=CreationForm
    success_url=reverse_lazy("login") #перенаправление после отправки формы
    template_name="signup.html"



# Create your views here.

def get_name(request):
    if request.method=='POST':
        form=Name(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thank-you/')
    else:
        form=Name()
    return render(request, 'name.html', {'form':form})