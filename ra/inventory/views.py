from django.shortcuts import get_object_or_404, render
from inventory.models import InventoryItem, InventoryEvent, IMGFile
from inventory.forms import IMGForm

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def inventory(request):
    logged_in = False
    itemList = InventoryItem.objects.all()

    if request.user.is_authenticated():
        logged_in = True

    return render(request, 'inventory/inventory.html', {'item_list' : itemList, 'logged_in' : logged_in})

@xframe_options_exempt
@csrf_exempt
def item_details(request, item_id):
    logged_in = False
    form = None
    inv_item = get_object_or_404(InventoryItem, pk=item_id)
    images = IMGFile.objects.filter(item=item_id)
    
    if request.user.is_authenticated():
        logged_in = True
        form = IMGForm()

    if request.method == 'POST' and logged_in == True:
        form = IMGForm(request.POST, request.FILES)
        if form.is_valid():
            pic = IMGFile(
                the_file = request.FILES['imgfile'],
                name = request.FILES['imgfile'].name,
                item = inv_item,
                file_size = request.FILES['imgfile'].size
                )
            pic.save()
    
    return render(request, 'inventory/item.html', {
            'item':inv_item,
            'images':images,
            'item_id':item_id,
            'logged_in':logged_in,
            'form':form})    

    

