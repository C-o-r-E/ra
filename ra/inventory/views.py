from django.shortcuts import get_object_or_404, render
from inventory.models import InventoryItem, InventoryEvent

def inventory(request):
    logged_in = None
    itemList = InventoryItem.objects.all()

    if request.user.is_authenticated:
        logged_in = True

    return render(request, 'inventory/inventory.html', {'item_list' : itemList, 'logged_in' : True})

def item_details(request, item_id):
    item = get_object_or_404(InventoryItem, pk=item_id)

    return render(request, 'inventory/item.html', {'item' : item})
