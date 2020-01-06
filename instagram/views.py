from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Accounts
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout

def agram(request):
    accounts=Accounts.all_accounts()
    return  render(request,'insta/home.html',{"accounts":accounts})



# def search_results(request):
    
#     if 'name' in request.GET and request.GET["name"]:
#         search_term = request.GET.get("name")
#         searched_name = Accounts.search_by_name(search_term)
#         message = f"{search_term}"

#         return render(request, 'insta/search.html',{"message":message,"name": searched_name})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'insta/search.html',{"message":message})
 

@login_required(login_url="/accounts/login/")
def logout(request):
  
  logout(request)
  return redirect('home')


@login_required(login_url = '/accounts/login/')
def profile(request):
    my_posts = Image.user_pics(request.user)
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