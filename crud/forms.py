from django import forms
from .models import Pegawaiudb

class PegawaiudbForm(forms.ModelForm):
    class Meta:
        model = Pegawaiudb
        fields = '__all__'