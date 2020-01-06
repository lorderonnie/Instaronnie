from django.shortcuts import get_object_or_404, redirect, render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Photos,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from .forms import EditProfileForm,Loginform,RegisterForm,NewPostForm

 
@login_required(login_url="/accounts/login/") 
def Home(request):
    home = Home.all_accounts()
    return  render(request,'insta/home.html',{"home":home})

def like(request):
    photos = get_object_or_404(Photos,id=request.POST.get('ig_pic_id'))
    user = request.User
    photos.likes.add(user)
    return (redirect,'timeline')

@login_required(login_url = '/accounts/login/')
def new_post(request):
    if request.method=='POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('timeline')

    else:
        form = NewPostForm()
        
    return render(request,'new_post.html',{'form':form})


def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_name = search_results.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'insta/search.html',{"message":message,"name": searched_name})

    else:
        message = "You haven't searched for any term"
        return render(request, 'insta/search.html',{"message":message})
 

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
                return redirect('home')
        else:
            messages.info(request,'passwords should match')
            return redirect('register')
        
    else:
        return render(request,'registration/registration_form.html')

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url = '/accounts/login/')
def profile(request):
  my_posts = Photos.user_pics(request.user)
  return render(request,'profile.html',{'my_posts':my_posts})

@login_required(login_url = '/accounts/login/')
def edit_profile(request):
    if request.method=='POST':
      form = EditProfileForm(request.POST,request.FILES,instance=request.user.profile)
      if form.is_valid():
          form.save()
          return redirect('profile')

      else:
          form = EditProfileForm(instance=request.user)
      return render(request,'profile.html',{'form':form})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    