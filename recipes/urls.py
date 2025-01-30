from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('recipes/', views.recipe_page, name='recipe_page'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name="recipe_detail"),  # Added trailing slash
    # Page for adding a new recipe.
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    # Page for adding ingredients
    path('add_ingredient/<int:recipe_id>/', views.add_ingredient, name='add_ingredient'),
    # Page for adding instructions
    path('add_instructions/<int:recipe_id>', views.add_instructions, name='add_instructions'),
    # Page for editing ingredients
    path('edit_ingredient/<int:ingredient_id>/', views.edit_ingredient, name='edit_ingredient'),
    # Page for editiing instructions
    path('edit_instructions/<int:instruction_id>/', views.edit_instructions, name='edit_instructions'),
    # Page for deleting recipe:
    path('recipe/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    # Page for deleting instructions
    path('instruction/<int:instruction_id>/delete/', views.delete_instruction, name='delete_instruction'),
    # Page for deleting ingredients
    path('ingredient/<int:ingredient_id>/delete/', views.delete_ingredient, name='delete_ingredient'),
]
