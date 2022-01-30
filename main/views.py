from django.shortcuts import render, HttpResponse

# Create your views here.
from main import models
from main.models import Product


def index(request):
    a = Product.objects.all()
    print(a)
    return HttpResponse(a[0].productvariant_set.all())
    # return render(request, template_name="main.html")
