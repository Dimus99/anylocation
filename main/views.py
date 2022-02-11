from django.shortcuts import render, HttpResponse

from main.models import Product, ProductType, Page


def index(request):
    url = request.path[1:]
    page = Page.objects.filter(slug=url).first()
    resp = None
    if page:
        types = page.product_type_set()
        resp = get_page(request, page.slug, types)
    return resp if resp else HttpResponse("error" + url)


# принимает название header, типы товаров, включающих в себя товары
# возвращает отрендеренную страницу
def get_page(request, header, types):
    # header + main + footer

    return HttpResponse(str([str(i) for i in types]))
