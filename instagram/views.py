from django.shortcuts import get_object_or_404, redirect, render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Photos,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UpdateProfileForm,UserUpdateform,Loginform,RegisterForm,NewPostForm
from .models import Photos,Profile,Comments
from .email import send_register_confirm_email

# @login_required(login_url="/accounts/login/") 
def Gram(request):
    photo = Photos.objects.all()
    return  render(request,'home.html',{"photo":photo})

def like(request):
    photos = get_object_or_404(Photos,id=request.POST.get('picture_id'))
    user = request.User
    photos.likes.add(user)
    return (redirect,'home')

@login_required(login_url = '/accounts/login/')
def new_post(request):
    if request.method=='POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('home')

    else:
        form = NewPostForm()
        
    return render(request,'new_post.html',{'form':form})


def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_name = search_results.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"name": searched_name})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
 

@login_required(login_url="/accounts/login/")
def logout(request):
  
  logout(request)
  return redirect('home')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name =request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 =request.POST['password1']
        
        if password1 == password:
            if User.objects.filter(username = username):
                messages.info(request,'This username is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,password = password,email = email,first_name = first_name,last_name = last_name,)
                user.save()
                send_register_confirm_email(username,email)
                return redirect('home')
        else:
            messages.info(request,'passwords should match')
            return redirect('register')
        
    else:
        return render(request,'registration/registration_form.html')

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    name = request.user
    profile = Profile.get_profile_by_name(name)
    photos = Photos.get_images_by_name(name)

    return render(request,"profile.html",{"profile":profile,"photos":photos,"name":name})
    
@login_required
def updateprofile(request):
   
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        form1 = UserUpdateform(request.POST,instance=request.user)
        if form.is_valid() and form1.is_valid():
            form1.save() 
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user.profile)
        form1 = UserUpdateform(instance=request.user)
    return render(request,"updateprofile.html",{"form":form,"form1":form1})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    