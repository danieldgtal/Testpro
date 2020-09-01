from django.urls import path
from .views import News, Home, Contact

urlpatterns = [
    path('', Home, name='home'),
    path('news/', News, name='news'),
    path('contact/', Contact, name='contact'),
]
