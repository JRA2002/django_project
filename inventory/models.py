from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    unit_price = models.FloatField(default=0)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=4,choices=[('kg','kg'),('lt','lt'),('unt','unt')])

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return '/inventory/'

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class RecipeRequirements(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    
    def __str__(self):
        return str(self.menuitem)

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.menu_item)
    
    def total_price(self):
        return self.quantity*self.menu_item.price
    