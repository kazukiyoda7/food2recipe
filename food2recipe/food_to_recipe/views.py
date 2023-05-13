from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView


from .forms import RecipeForm

from .get_recipe import get_recipes

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
    
class MemberView(TemplateView):
    template_name = "member.html"
    
class RegisterView(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("food_to_recipe:index")
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)