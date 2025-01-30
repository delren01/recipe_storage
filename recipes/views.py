from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Recipe, Ingredient, Instruction
from .forms import RecipeForm, IngredientForm, InstructionForm
# Create your views here.
def index(request):
    """The home page for Recipes Website"""
    return render(request, 'recipes/index.html')

@login_required
def recipe_page(request):
    """Show all created recipes."""
    recipes = Recipe.objects.filter(owner=request.user).order_by('updated_at')
    context = {'recipes': recipes}
    return render(request, 'recipes/recipe_page.html', context)

@login_required
def recipe_detail(request, recipe_id):
    """Show a single recipe and its details."""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    check_recipe_owner(request, recipe)
    
    instructions = recipe.instruction_steps.all().order_by('id')
    ingredients = recipe.ingredients.all().order_by('name')
    context = {'recipe': recipe, 'instructions': instructions, 'ingredients': ingredients}
    return render(request, 'recipes/recipe_detail.html', context)

# When user initially requests this page, their browser will send a GET request.
@login_required
def new_recipe(request):
    """Add a new recipe."""
    # Once they've filled out the form, their browser will send a POST request.
    # We use an 'if' test to determine whether the request method is GET or POST
    # If the request method IS NOT POST, we need to return a blank form.
    if request.method != 'POST':
        # No data submitted; create a blank form
        # We make an instance of RecipeForm and assign it to variable 'form' and send it to context dictionary
        form = RecipeForm()
    # If request method IS POST, else block processes the data submitted.
    else:
        # POST data submitted; process data
        # We make instance of RecipeForm and pass the data entered by user and assign to 'request.POST'
        form = RecipeForm(data=request.POST)
        # The is_valid() method checks that all required fields have been filled in.
        # And data entered matches the field types expected.
        if form.is_valid():
            # We call save() which writes the data from the form to the database.
            new_recipe = form.save(commit=False)
            new_recipe.owner = request.user
            new_recipe.save()
            # redirect() function takes in the name of a view and redirects user to the page associated with that view.
            return redirect('recipes:recipe_page')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'recipes/new_recipe.html', context)

@login_required
def add_ingredient(request, recipe_id):
    """Add an ingredient"""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    check_recipe_owner(request, recipe)
    if request.method != 'POST':
        form = IngredientForm()
    else:
        form = IngredientForm(data=request.POST)
        if form.is_valid():
            new_ingredient = form.save(commit=False)
            new_ingredient.recipe = recipe
            new_ingredient.save()
            return redirect('recipes:recipe_detail', recipe_id=recipe_id)
    context = {'recipe': recipe, 'form': form}
    return render(request, 'recipes/add_ingredient.html', context)

@login_required
def add_instructions(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    check_recipe_owner(request, recipe)
    if request.method != 'POST':
        form = InstructionForm()
    else:
        form = InstructionForm(data=request.POST)
        if form.is_valid():
            new_instruction = form.save(commit=False)
            new_instruction.recipe = recipe
            new_instruction.save()
            return redirect('recipes:recipe_detail', recipe_id=recipe_id)
    context = {'recipe': recipe, 'form': form}
    return render(request, 'recipes/add_instructions.html', context)

@login_required
def edit_ingredient(request, ingredient_id):
    """Edit an existing ingredient."""
    ingredient = Ingredient.objects.get(id=ingredient_id)
    recipe = ingredient.recipe
    check_recipe_owner(request, recipe)
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry
        form = IngredientForm(instance=ingredient)
    else:
        # POST data submitted; process data
        form = IngredientForm(instance=ingredient, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe_detail', recipe_id=recipe.id)
    context = {
        'ingredient': ingredient,
        'recipe': recipe,
        'form': form,
    }
    return render(request, 'recipes/edit_ingredient.html', context)

@login_required
def edit_instructions(request, instruction_id):
    """Edit an existing instructions"""
    instruction = Instruction.objects.get(id=instruction_id)
    recipe = instruction.recipe
    check_recipe_owner(request, recipe)
    if request.method != "POST":
        # Initial requests; pre-fill form with current entry
        # The argument 'instance=instruction' tells Django to create form, prefilled with information
        # From the existing instruction object. The user will see their existing data and be able to edit data.
        form = InstructionForm(instance=instruction)
    else:
        # POST data submitted; process data
        form = InstructionForm(instance=instruction, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe_detail', recipe_id=recipe.id)
    context = {
        'instruction': instruction,
        'recipe': recipe,
        'form': form,
    }
    return render(request, 'recipes/edit_instructions.html', context)

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == "POST":
        recipe.delete()
        return redirect('recipes:recipe_page')
    context = {'recipe': recipe}
    return render(request, 'recipes/delete_recipe.html', context)

@login_required 
def delete_instruction(request, instruction_id):
    instruction = get_object_or_404(Instruction, id=instruction_id)
    recipe_id = instruction.recipe.id # Get recipe ID before deleting

    if request.method == "POST":
        instruction.delete()
        return redirect('recipe:recipe_detail', recipe_id=recipe_id)
    context = {'instruction': instruction}
    return render(request, 'recipes/delete_instruction.html', context)

@login_required
def delete_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    recipe_id = ingredient.recipe.id # Get recipe ID before deleting

    if request.method == "POST":
        ingredient.delete()
        return redirect('recipe:recipe_detail', recipe_id=recipe_id)
    context = {'ingredient': ingredient}
    return render(request, 'recipes/delete_ingredient.html', context)

def check_recipe_owner(request, recipe):
    """Groups repeated codes into a function."""
    if recipe.owner != request.user:
        raise Http404