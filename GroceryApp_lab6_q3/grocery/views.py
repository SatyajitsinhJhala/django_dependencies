from django.shortcuts import render
from .models import GroceryItem

def index(request):
    items = GroceryItem.objects.all()
    return render(request, 'index.html', {'items': items})

def add_item(request):
    selected_ids = request.POST.getlist('items')
    selected_items = GroceryItem.objects.filter(id__in=selected_ids)
    return render(request, 'result.html', {'selected_items': selected_items})
