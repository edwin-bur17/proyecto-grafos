from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, "home.html")

def info(request):
    return render(request, "info.html")

@csrf_exempt
def add_product(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product = {
                "name": data.get("name"),
                "brand": data.get("brand"),
                "product_type": data.get("product_type"),
                "presentation": data.get("presentation"),
            }
            from . import views_logic
            views_logic.add_product_to_list(product)
            return JsonResponse({"message": "Product added successfully"})
        except Exception as e:
            return HttpResponseBadRequest(f"Error: {str(e)}")
    else:
        return HttpResponseBadRequest("Only POST method allowed")

def list_products(request):
    from . import views_logic
    products = views_logic.get_all_products()
    return JsonResponse({"products": products})

def search_category(request):
    category_name = request.GET.get("name")
    if not category_name:
        return HttpResponseBadRequest("Missing 'name' parameter")
    from . import views_logic
    category_node = views_logic.find_category_node(category_name)
    if category_node:
        children = [child.name for child in category_node.children]
        return JsonResponse({"category": category_node.name, "children": children})
    else:
        return JsonResponse({"error": "Category not found"}, status=404)

def calculate_route(request):
    start = request.GET.get("start")
    end = request.GET.get("end")
    if not start or not end:
        return HttpResponseBadRequest("Missing 'start' or 'end' parameters")
    from . import views_logic
    route = views_logic.calculate_route(start, end)
    if route:
        return JsonResponse({"route": route})
    else:
        return JsonResponse({"error": "No route found"}, status=404)
