from django.contrib import admin
from .models import Tache,Categorie

# Register your models here.

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom_categorie',)
