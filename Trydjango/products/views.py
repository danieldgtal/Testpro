from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product
from django.views.generic.edit import DeleteView


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


def product_create_view(request):
    initial = {
        'title': "My new Awesome font",
        'description': "A very nice way to describe a product",
        'price': 300,
        }
    # obj = Product.objects.get(id=1)
    # my_form = ProductForm(request.POST or None, instance=obj)
    my_form = ProductForm(request.POST or None)
    if my_form.is_valid():
        print(my_form.cleaned_data)
        Product.objects.create(**my_form.cleaned_data)
        my_form.save()
        # form.ProductForm()
    else:
        print(my_form.errors)
    context = {
        'form': my_form
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


def dynamic_lookup_view(request, my_id):
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    obj = get_object_or_404(Product, id=my_id)
    # obj = Product.objects.get(id=my_id)
    context = {
        'object': obj
    }
    return render(request, "products/product_details.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    # POST request
    if request.method == "POST":
        obj.delete()
        return redirect('../..')
    context = {
        'object': obj
    }
    return render(request, "products/product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


