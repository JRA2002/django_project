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
from django.db.models import Sum
def logout_request(request):
  logout(request)
  return redirect("home")

class InventoryView(LoginRequiredMixin,ListView):
    model = Ingredient
    template_name = 'inventory/inventory.html'


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

class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirements_set.all():
                total_cost += recipe_requirement.ingredients.unit_price * \
                    recipe_requirement.quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context