from django.core.serializers import json
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def index(request):
    item_count=0
    if request.is_ajax():
        data = {"item_count":item_count}
        return JsonResponse(data)
    return render(request, "index.html",{"item_count":item_count})


def add(request):
    if request.method == 'POST':
        if request.is_ajax():
            item_name = request.POST['item_name']
            item_price = request.POST['item_price']
            item_count = request.POST['item_count']

            item_counter = int (item_count)
            item_counter += 1
            data = {"item_name": item_name, "item_price": item_price,"item_count":item_counter}
        # Returning same data back to browser.It is not possible with Normal submit

            return JsonResponse(data)
    return render(request, "index.html")
