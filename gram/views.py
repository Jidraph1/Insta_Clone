from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Image, Profile, Like
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
