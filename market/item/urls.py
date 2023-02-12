from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('newItem/', views.newItem, name='addNewItem'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/makesold/', views.makeSold, name='makesold'),
    path('<int:pk>/edit/', views.editItem, name='edit'),
    path('', views.items, name='items'),

]