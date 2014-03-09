from django.shortcuts import get_object_or_404, render
from inventory.models import InventoryItem, InventoryEvent

def inventory(request):
    itemList = InventoryItem.objects.all()

    return render(request, 'inventory/inventory.html', {'item_list' : itemList})

def item_details(request, item_id):
    item = get_object_or_404(InventoryItem, pk=item_id)

    return render(request, 'inventory/item.html', {'item' : item})
