import main.views as views

from django.urls import path

urlpatterns = [

    path('viezdnoy-kokteilniy-bar', views.index),
    path('viezdnoi-kofe-bar', views.coffePage),
    path('viezdnoi-bar-goryachie-napitki', views.hotDrinks),
    path('viezdnoi-bar-bezalkogolnie-napitki', views.index),
    path('streetfood-catering', views.index),
    path('grill-and-bbq', views.index),
    path('fun-catering', views.index),
    path('coffee-breaks', views.index),
    path('interactive', views.index),
    path('catering-na-vistavku', views.index),
    path('branding', views.index),
    path('viezdnoi-bar-na-23-fevralya', views.index),
    path('viezdnoi-bar-na-8-marta', views.index),
    path('octoberfest', views.index),
    path('rozhdestvenskie-yarmarki', views.index),
    path('ZOZH', views.index),
    path('', views.index),
]
