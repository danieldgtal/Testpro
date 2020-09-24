from django.urls import path
from .views import NewsP, Home, Contact,register, addUser, modelforms, addModalForm

urlpatterns = [
    path('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path('contact/', Contact, name='contact'),
    path('signup/',register,name='register'),
    path('addUser/', addUser, name='addUser'),
    path('forms/', modelforms, name='modelform'),
]
