from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("info/", views.info, name="info"),
    path("add_product/", views.add_product, name="add_product"),
    path("list_products/", views.list_products, name="list_products"),
    path("search_category/", views.search_category, name="search_category"),
    path("calculate_route/", views.calculate_route, name="calculate_route"),
]
