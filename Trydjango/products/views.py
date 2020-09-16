from django.shortcuts import render
from .forms import ProductForm, RawProductForm
from .models import Product


# set initial data on form
def render_initial_data(request):
    initial_data = {
        "title": "This is awesome title"
    }
    form = RawProductForm(request.POST or None, initial=initial_data)
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
# Create your views here.
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form':my_form
#     }
#     return  render(request,"products/product_create.html", context)
# def product_create_view(request):
#     print(request.GET)
#     print(request.POST)
#     context = {}
#     return  render(request,"products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title' : obj.title,
    #     'description': obj.description,
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_details.html", context)

