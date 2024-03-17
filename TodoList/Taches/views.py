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


class TacheUpdateView(UpdateView):
    model = Tache
    form_class = CreateTacheForm
    # fields = ['nom_tache','date','heure_debut','heure_fin','priorite','statut','categorie','responsable','commentaire']
    success_url = reverse_lazy("Taches:taches")
    template_name = "tache/tache_create_view.html"

    def form_valid(self, form):
        messages.success(self.request,"La tache a été mise à jour avec succès")
        return super(TacheUpdateView, self).form_valid(form)


class TacheDeleteView(DeleteView):
    model = Tache
    context_object_name = 'tache'
    success_url = reverse_lazy("Taches:taches")
    template_name = "tache/tache_confirmation_delete.html"

    def form_valid(self, form):
        messages.success(self.request,"tache supprimée avec succès")
        return super(TacheDeleteView,self).form_valid(form)


class TacheDetailView(DetailView):
    model = Tache
    context_object_name = 'tache'
    template_name = "tache/tache_detail_view.html"


