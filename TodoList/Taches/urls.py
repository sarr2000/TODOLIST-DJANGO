from django.urls import path
from .import views

app_name = 'Taches'

urlpatterns = [

    # path('', views.home, name='home'),
    # path('contacts/', views.create_view1, name='contact'),

    path('categories/', views.CategorieListView.as_view(), name='categories'),
    path('categorieForm/', views.CategorieCreateview.as_view(), name='categorieForm'),
    path('taches/', views.TacheListView.as_view(), name='taches'),
    path('tacheForm/', views.TacheCreateview.as_view(), name='tacheForm'),
]