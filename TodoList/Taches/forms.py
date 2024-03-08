from django import forms
from .models import  Tache,Categorie



class CreateCategorieForm(forms.ModelForm):

    class Meta:
        model= Categorie

        fields = [
            "nom_categorie",
        ]

        widgets = {
            'nom_categorie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer nom categorie'}),

        }


class CreateTacheForm(forms.ModelForm):

    class Meta:
        model= Tache

        fields = [
            "nom_tache",
            "date",
            "heure_debut",
            "heure_fin",
            "statut",
            "priorite",
            "categorie",
            "responsable",
            "commentaire",
        ]

        widgets = {
            'nom_tache': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer nom tache'}),
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy (DOB)','class': 'form-control'}),
            'heure_debut': forms.TimeInput(attrs={'type': 'time','format':'%H:%M','class': 'form-control'}),
            'heure_fin': forms.TimeInput(attrs={'type': 'time','format':'%H:%M','class': 'form-control'}),
            'priorite': forms.Select(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
            'commentaire': forms.Textarea(attrs={'class': 'form-control'})
        }



