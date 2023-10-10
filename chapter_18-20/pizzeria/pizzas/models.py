from django.db import models

class Pizza(models.Model):
    """A pizza the pizzeria offers"""
    name = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name

class Topping(models.Model):
    """Topping on the pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representing the topping"""
        return f"{self.name}"