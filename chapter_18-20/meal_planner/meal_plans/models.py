from django.db import models

class MealPlan(models.Model):
    """A meal plan for the user"""
    plan = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of the meal plan"""
        return self.plan