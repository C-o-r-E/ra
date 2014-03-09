from django.contrib import admin
from inventory.models import InventoryItem, InventoryEvent

admin.site.register((InventoryItem, InventoryEvent))


