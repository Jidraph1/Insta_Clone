from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Image, Profile, Like
from django.contrib.auth.models import User
from .forms import ImageForm, ProfileForm, CommentForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    images = Image.objects.all().order_by('-posted_at')
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.save()
            return redirect('index')
    
    else:
        form = CommentForm()
        
    return render(request, 'index.html',{"current_user": current_user, "images":images, "profiles":profiles, "form":form})

@login_required(login_url='/accounts/login/')
def post(request):
    
    if request.method == 'POST':  
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('index')
    
    else:
        form = ImageForm()
        return render(request, 'post.html', {'form':form})

@login_required
def search_results(request):
  if 'search_user' in request.GET and request.GET["search_user"]:
    search_term = request.GET.get('search_user')
    searched_users = Profile.search_profile(search_term)
    message = f"{search_term}"
    return render(request,'search.html',{"message":message,"users":searched_users})
  else:
    message="You haven't searched for any term."  
    return render(request,'search.html',{"message":message,"users":searched_users})