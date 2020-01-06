from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Accounts

def agram(request):
    accounts=Accounts.all_accounts()
    return  render(request,'agram/home.html',{"accounts":accounts})



def search_results(request):
    
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_name = Accounts.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'agram/search.html',{"message":message,"name": searched_name})

    else:
        message = "You haven't searched for any term"
        return render(request, 'agram/search.html',{"message":message})
 







