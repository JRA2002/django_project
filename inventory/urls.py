
from django.urls import path,include
from . import views

urlpatterns = [
    path('inventory/', views.InventoryView.as_view(), name='inventory'),
    path('', views.HomeView.as_view(), name='home'),
    path('inventory/<pk>/delete', views.DeleteIngredientView.as_view(), name='delete_ingredient'),
    path('menu/', views.MenuItemView.as_view(), name='menu_item'),
    path('purchase/', views.PurchaseView.as_view(), name='purchase'),
    path('inventory/add_ingredient/', views.AddIngredientView.as_view(), name='add_ingredient'),
    path('menu/add_menu_item/', views.AddMenuItemView.as_view(), name='add_menu_item'),
    path('menu/<pk>/add_recipe_requirements/', views.AddRecipeRequirementsView.as_view(), name='add_recipe_requirements'),
    path('purchase/add_purchase/', views.AddPurchaseView.as_view(), name='add_purchase'),
    path('inventory/<pk>/update', views.UpdateIngredientView.as_view(), name='update_ingredient'),
    path('logout/', views.LogoutView, name="logout"),
    path("accounts/", include("django.contrib.auth.urls"), name="login"),
]