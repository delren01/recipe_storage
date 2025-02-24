from django import forms
# from .models.py, we import the 'Recipe' class we created
from .models import Recipe, Ingredient, Instruction

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'cooking_time_hours', 'cooking_time_minutes', 'category']
        labels = {
            'name': 'Recipe Name',
            'cooking_time_hours': 'Cooking Time (Hours)',
            'cooking_time_minutes': 'Cooking Time (Minutes)',
            'category': 'Category'
        }

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'cooking_time_hours': forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            'cooking_time_minutes': forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            'category': forms.Select(attrs={"class": "form-select"})
        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']
        labels = {
            'name': 'Ingredient Name',
            'quantity': 'Quantity',
            'unit': 'Unit of Measurement (ex. pinch, dash, cups, tbsp, tsp, pcs)'
        }
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'quantity': forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            'unit': forms.TextInput(attrs={"class": "form-control"})
        }

class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['instruction_text']
        labels = {'instruction_text': "Instructions"}
        widgets = {
            'instruction_text': forms.Textarea(attrs={"class": "form-control"})
        }
