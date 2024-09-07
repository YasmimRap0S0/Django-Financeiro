from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={"placeholder": "Nome completo", "class": "rec-nome"}),
            'email': forms.TextInput(attrs={"placeholder": "Email", "class":"RecEmail"}),
            'senha': forms.PasswordInput(attrs={"placeholder": "Senha", "class":"RecSenha"})
        }