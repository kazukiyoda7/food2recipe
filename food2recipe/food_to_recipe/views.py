from django.shortcuts import render

from .forms import RecipeForm

from .get_recipe import get_recipes

# Create your views here.
# top page
def index(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            input_food = form.cleaned_data['input_food']
            recipe_ranking = get_recipes(input_food)
            return render(request, 'result.html', {'input_food': input_food, 'recipe_ranking':recipe_ranking})
    else:
        form = RecipeForm()
        return render(request, 'index.html', {'form': form})
    

