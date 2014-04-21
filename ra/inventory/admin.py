from django.contrib import admin
from inventory.models import InventoryItem, InventoryEvent, IMGFile

admin.site.register((InventoryItem, InventoryEvent, IMGFile))


