from django import forms
from .models import Myfood

class RecipeForm(forms.Form):
    input_food = forms.CharField(max_length=50, required=True, label="食材を入力")
    

class MyfoodForm(forms.ModelForm):
    number = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 11)], label="個数")
    class Meta:
        model = Myfood
        fields = ("food", "number")