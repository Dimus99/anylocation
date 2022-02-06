from django.shortcuts import render, HttpResponse

# Create your views here.
from main import models
from main.models import Product, ProductType


def index(request):
    a = Product.objects.all()
    print(a)
    return HttpResponse(a[0].productvariant_set.all())
    # return render(request, template_name="main.html")


def coffePage(request):
    type_names = [
        ''
    ]
    types = ProductType.objects.filter(name__in=type_names)


def get_page(request, header, types):
    return None


def hotDrinks(request):
    return None
