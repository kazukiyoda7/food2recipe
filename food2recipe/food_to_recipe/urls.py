from django.urls import path
from . import views


app_name = 'food_to_recipe'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search-recipe/', views.search_recipe, name='search-recipe'),
    path('login/', views.RecipeLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page="food_to_recipe:index"), name='logout'),
    # path('member/', views.MemberView.as_view(), name='member'),
    path('member/', views.member, name='member'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('add-food/', views.AddFoodView.as_view(), name='add-food'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
]
