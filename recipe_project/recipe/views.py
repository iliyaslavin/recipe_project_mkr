from django.shortcuts import render, get_object_or_404
from .models import Recipe

def main(request):
    recipes = Recipe.objects.filter(date__year=2023)
    return render(request, 'recipe/main.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})
