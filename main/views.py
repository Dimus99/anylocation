from django.shortcuts import render, HttpResponse

from main.models import Product, ProductType, Page


def main(request):
    return HttpResponse("main page")


def index(request):
    url = request.path[1:]
    page = Page.objects.filter(slug=url).first()
    resp = None
    if page:
        types = page.producttype_set.all()
        resp = get_page(request, page.slug, types)
    return resp if resp else HttpResponse("error" + url)


# принимает название header, типы товаров, включающих в себя товары
# возвращает отрендеренную страницу
def get_page(request, header, types):
    # header + main + footer
    serial_types = [
        {"name": product_type.name,
         "description": product_type.description,
         "products": serialize_products(product_type.product_set.all())
         }
        for product_type in types
    ]
    data = {"header": header, "types": serial_types}
    return render(request, "body.html", context=data)


def serialize_variants(variants):
    return [
        {
            "name": v.name,
            "price": v.price
        }
        for v in variants
    ]


def serialize_products(products):
    return [
        {
            "name": n.name,
            "description": n.description,
            "cost": n.cost,
            "img": n.img.path,  # TODO: need serialize
            "additional_img": n.additional_img,
            "variants": serialize_variants(n.productvariant_set.all())
        } for n in products
    ]
