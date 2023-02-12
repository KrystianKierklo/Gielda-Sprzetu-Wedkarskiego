from django.shortcuts import render, redirect
from django.db.models import Count

from item.models import Category, Item
from .forms import SingupForm
# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[0:8]
    item_count = Item.objects.filter(is_sold=False).count
    categories = Category.objects.filter()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'item_count': item_count,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = SingupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

