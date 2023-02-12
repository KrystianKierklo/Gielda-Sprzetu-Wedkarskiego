from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from item.models import Item

@login_required()
def index(request):
    items = Item.objects.filter(created_by=request.user, is_sold=False)
    my_items_count = Item.objects.filter(created_by=request.user, is_sold=False).count
    items_sold = Item.objects.filter(created_by=request.user, is_sold=True)
    items_sold_count = Item.objects.filter(created_by=request.user, is_sold=True).count

    return render(request, 'dashboard/index.html', {
        'items': items,
        'my_items_count': my_items_count,
        'items_sold': items_sold,
        'items_sold_count': items_sold_count,
    })



