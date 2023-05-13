from django import forms

class RecipeForm(forms.Form):
    input_food = forms.CharField(max_length=50)
