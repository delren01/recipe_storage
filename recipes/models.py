from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """
    Represents a classificiation or grouping of recipes.
    Examples of categories include 'Breakfast', 'Dessert' or 'Main Course'
    Each recipe belongs to one category.
    """
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'
    DESSERT = 'dessert'
    
    CATEGORY_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (DESSERT, 'Dessert'),
    ]

    name = models.CharField(max_length=255, choices=CATEGORY_CHOICES, unique=True)
    description = models.TextField(blank=True, null=True, help_text="Optional description of category")

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return dict(self.CATEGORY_CHOICES).get(self.name, self.name)

class Recipe(models.Model):
    """
    Represents a single recipe in the app.
    Contains basic information like recipe name, description of the dish,
    and additional details like cooking time or difficulty level.
    """
    name = models.CharField(max_length=300)
    instructions = models.TextField()
    cooking_time_hours = models.IntegerField(default=0, help_text="Cooking time in hours.")
    cooking_time_minutes = models.IntegerField(default=0, help_text="Cooking time in minutes.")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Instruction(models.Model):
    """
    Represents a single step or instruction for a recipe.
    Each instruction is linked to a Recipe.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='instruction_steps')
    instruction_text = models.TextField()

    def __str__(self):
        return self.instruction_text
    
class Ingredient(models.Model):
    """
    Represents an ingredient used in a recipe.
    
    Each ingredient includes its name, the quantity used, and the unit of measurement.
    Ingredients can belong to multiple recipes, linking them through the `recipe` field.
    """
    name = models.CharField(max_length=300, help_text="The name of the ingredient (e.g., 'Sugar').")
    quantity = models.FloatField(help_text="The quantity of the ingredient.")
    unit = models.CharField(max_length=10, help_text="The unit of measurement for the quantity.")
    recipe = models.ForeignKey(
        'Recipe', 
        on_delete=models.CASCADE, 
        related_name='ingredients',
        help_text="The recipe this ingredient belongs to."
    )

    def __str__(self):
        """
        String representation of the ingredient, showing the quantity, unit, and name.
        """
        return f"{self.quantity} {self.unit} of {self.name}"

