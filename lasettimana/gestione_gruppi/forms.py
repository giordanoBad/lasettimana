from django import forms
from .models import Gruppo, MembroGruppo


class GruppoForm(forms.ModelForm):
    numero_membri = forms.IntegerField(label='Numero Membri')
    data_arrivo = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    data_partenza = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


    class Meta:
        model = Gruppo
        fields = ['nome', 'cognome', 'numero_telefono', 'data_arrivo', 'data_partenza', 'numero_membri']

class MembroGruppoForm(forms.ModelForm):
    data_arrivo = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    data_partenza = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = MembroGruppo
        fields = ['nome', 'cognome', 'numero_telefono','data_arrivo','data_partenza']
        