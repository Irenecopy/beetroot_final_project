from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.

class Category(models.Model):
    """
    Model representing an expense category (e.g. Food, Transport).
    """
    name = models.CharField(max_length=200, help_text="Enter an expense category (e.g. Food, Transport)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Expense(models.Model):
    """
    Model representing an expense.
    """
    amount_of_expenses = models.IntegerField(max_length=200)
    budget = models.ForeignKey('Budget', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because expense can only have one budget, but budgets can have multiple expenses
    # Budget as a string rather than object because it hasn't been declared yet in the file.
    comment = models.TextField(max_length=1000, help_text="Enter a comment of the expense")
    category = models.ForeignKey(Category, help_text="Select a category for this expense")
    # Foreign Key used because category can contain many expenses. Expenses can only have one category.
    # Genre class has already been defined so we can specify the object above.
    date_of_expense = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular expense instance.
        """
        return reverse('book-detail', args=[str(self.id)])