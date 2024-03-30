from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView
from .models import MenuItem, Purchase, RecipeRequirements, Ingredient
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .forms import IngredientForm, MenuItemForm,RecipeRequirementsForm,PurchaseForm
# Create your views here.
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


def logout_view(request):
  logout(request)
  return redirect("home")
class InventoryView(LoginRequiredMixin,ListView):
    model = Ingredient
    template_name = 'inventory/inventory.html'
    success_url = reverse_lazy('inventory')

class HomeView(TemplateView):
    template_name = 'inventory/home.html'

class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = 'inventory/delete_ingredient.html'
    success_url = '/inventory/'

class MenuItemView(ListView):
    model = MenuItem
    template_name = 'inventory/menu_item.html'

class PurchaseView(ListView):
    model = Purchase
    template_name = 'inventory/purchase.html'

class AddIngredientView(CreateView):
    model = Ingredient
    template_name = 'inventory/add_ingredient.html'
    form_class = IngredientForm
    success_url = reverse_lazy('inventory')

class AddMenuItemView(CreateView):
    model = MenuItem
    template_name = 'inventory/add_menu_item.html'
    form_class = MenuItemForm
    success_url = reverse_lazy('menu_item')

class AddRecipeRequirementsView(CreateView):
    model = RecipeRequirements
    template_name = 'inventory/add_recipe_requirements.html'
    form_class = RecipeRequirementsForm
    success_url = reverse_lazy('menu_item')
    
class AddPurchaseView(CreateView):
    model = Purchase
    template_name = 'inventory/add_purchase.html'
    form_class = PurchaseForm
    success_url = reverse_lazy('purchase')

class UpdateIngredientView(UpdateView):
    model = Ingredient
    template_name = 'inventory/update_ingredient.html'
    form_class = IngredientForm
    success_url = reverse_lazy('inventory')

def LogoutView(request):
  logout(request)
  return redirect("home")