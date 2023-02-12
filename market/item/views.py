from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Item, Category
# Create your views here.
from .forms import NewItemForm, EditItemForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk).order_by('-created_at')[0:5]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })

@login_required()
def newItem(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Dodaj nowe ogłoszenie'
    })

@login_required()
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

@login_required()
def makeSold(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.is_sold = True
    item.save()

    return redirect('dashboard:index')


@login_required()
def editItem(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edytuj przedmiot'
    })

def items(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)


    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if category_id:
        items = items.filter(category_id=category_id)

    items_count = items.count

    paginator = Paginator(items, 15)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)



    return render(request, 'item/items.html',{
        'items': items,
        'items_count': items_count,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'page': page
    })

