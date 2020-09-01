from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def Home(request):
    context= {
        "name":"Daniel",
        "number": 12345


    }
    return render(request,'index.html', context)


def News(request):

    return render(request,'news.html')

def Contact(request):
    return render(request,'contact.html')

