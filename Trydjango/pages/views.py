from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home_view(request,*args, **kwargs):
    print(args,kwargs)
    return render(request,"home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args,**kwargs):
    my_context = {
        "my_number"    : 12345,
        "this_is_true" :True,
        "title"      :'this is about django',
        "my_list"      :[123,234,345,"ABC"]
    }
    return render(request, "about.html", my_context)