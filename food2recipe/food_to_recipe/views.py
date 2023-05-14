from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

from .forms import RecipeForm, MyfoodForm

from .get_recipe import get_recipes

from .models import Recipe, Myfood

# Create your views here.
# top page
class IndexView(TemplateView):
    template_name = 'index.html'
    
def search_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            input_food = form.cleaned_data['input_food']
            recipe_ranking = get_recipes(input_food)
            
            # レシピの結果が見つかったら
            if len(recipe_ranking)!=0:
                recipe = Recipe(
                    user = request.user,
                    food = input_food,
                )
                recipe.save()
                return render(request, 'result.html', {'input_food': input_food, 'recipe_ranking':recipe_ranking})
            else:
                return render(request, 'failure.html')
    else:
        form = RecipeForm()
        return render(request, 'search-recipe.html', {'form': form})


class RecipeLoginView(LoginView):
    fields = "__all__"
    template_name = "login.html"
    
    def get_success_url(self):
        return reverse_lazy("food_to_recipe:member")
    
class MemberView(ListView):
    model = Recipe
    template_name = "member.html"
    context_object_name = "history_recipe"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.filter(user=user)
            print(queryset)
        return queryset

def member(request):
    model1 = Recipe.objects.filter(user=request.user)
    model2 = Myfood.objects.filter(user=request.user)
    context = {
        "recipes":model1,
        "myfoods":model2,
    }
    return render(request, 'member.html', context)
    
class RegisterView(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("food_to_recipe:index")
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
class AddFoodView(CreateView):
    model = Myfood
    form_class = MyfoodForm
    template_name = "add-food.html"
    success_url = reverse_lazy("food_to_recipe:member")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class EditView(UpdateView):
    model = Myfood
    form_class = MyfoodForm
    template_name = "add-food.html"
    success_url = reverse_lazy("food_to_recipe:member")

class DeleteView(DeleteView):
    model = Myfood
    template_name = "delete.html"
    success_url = reverse_lazy("food_to_recipe:member")
