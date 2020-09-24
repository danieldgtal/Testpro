from django.shortcuts import render, redirect
from .models import News
from .forms import RegistrationForm, RegistrationModal
from .models import RegistrationData
from django.contrib import messages


# Create your views here.
def Home(request):

    return render(request,'index.html')


def NewsP(request):
    obj = News.objects.get(id=1)
    context = {
        "data":obj
    }
    return render(request,'news.html')


def Contact(request):
    return render(request,'contact.html')


def register(request):
    context = {
        "form":RegistrationForm

    }

    return render(request,'signup.html',context)


def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(username = form.cleaned_data['username'],
                                    password = form.cleaned_data['password'],
                                    email = form.cleaned_data['email'],
                                    phone = form.cleaned_data['phone'],)

        myregister.save()
        messages.add_message(request,messages.SUCCESS,'You have Signup Successfully')

        return redirect('register')

def modelforms(request):

    context = {
        "modalform":RegistrationModal
    }

    return render(request,'modalform.html',context)
