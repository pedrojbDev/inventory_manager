from inventory.views import InventoryListView,NewIten,ItensDetailView,ItensUpdateView,ItensDeleteView
from accounts.views import login_view,register_view,logout_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/',InventoryListView.as_view(),name='inventory'),
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register'),
    path('logout/',logout_view,name='logout'),
    path('new_iten/',NewIten.as_view(),name='new_iten'),
    path('itens/<int:pk>/', ItensDetailView.as_view(), name='itens_detail'),
    path('itens/<int:pk>/update/',ItensUpdateView.as_view(),name='itens_update'),
    path('itens/<int:pk>/delete/',ItensDeleteView.as_view(),name='itens_delete'),
    
]
