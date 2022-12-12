from django.db import models
from django.db.models import Model

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Pizzas'
    
    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__():
        return f"{self.text[:50]}"


class Image(Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploa/')
    date_added = models.DateTimeField(auto_now_add=True)
