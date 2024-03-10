from django.shortcuts import render
from .models import Tache,Categorie,User
from django.views.generic import  CreateView,ListView,DeleteView,DetailView,UpdateView
from  .forms import CreateTacheForm,CreateCategorieForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class CategorieCreateview(CreateView):
    model =  Categorie
    template_name = "categorie/categorie_create_view.html"
    form_class = CreateCategorieForm
    success_url = reverse_lazy("Taches:categories")


class CategorieListView(ListView):
    model = Categorie
    context_object_name = "liste_des_categories"
    template_name = "categorie/categorie_list_view.html"


class TacheCreateview(CreateView):
    model =  Tache
    template_name = "tache/tache_create_view.html"
    form_class = CreateTacheForm
    success_url = reverse_lazy("Taches:taches")


class TacheListView(ListView):
    model = Tache
    context_object_name = "liste_des_taches"
    template_name = "tache/tache_list_view.html"


    # ********** filtrer les taches selon l'utilisateur connecté************'
    def get_queryset(self):
        queryset = super().get_queryset()
        u=self.request.user
        if u.username=='admin':
            return queryset
        else:
           return queryset.filter(responsable=u)





