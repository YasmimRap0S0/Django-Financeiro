from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={"placeholder": "Nome completo", "class": "Rec-nome", "style": "width: 400px; height: 52.20px; left: 148px; top: 365px; position: absolute; background: white; border-radius: 50px; border: 1px #7B7B7B solid"}),
            'email': forms.TextInput(attrs={"placeholder": "Email", "class":"RecEmail", "style": "width: 400px; height: 52.20px; left: 148px; top: 513px; position: absolute; background: white; border-radius: 50px; border: 1px #7B7B7B solid"}),
            'senha': forms.PasswordInput(attrs={"placeholder": "Senha", "class":"RecSenha", "style": "width: 400px; height: 52.20px; left: 148px; top: 679px; position: absolute; background: white; border-radius: 50px; border: 1px #7B7B7B solid"})
        }

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=150)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

