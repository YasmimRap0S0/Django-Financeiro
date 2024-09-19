from django import forms
from .models import Usuario, Receita, Balancete, Despesa


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

class AddBalanceteForm(forms.ModelForm):
    class Meta:
        model = Balancete
        fields = ['nome', 'data']
        widgtes = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nomeie o balancete'}), 
            'data' : forms.DateField()    
            }

class AddReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['nome', 'valor', 'balancete']
        widgets = {
            'balancete': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['balancete'].queryset = Balancete.objects.all().order_by('nome')

class AddDespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['nome', 'valor', 'balancete', 'foto_boleto']
        widgets = {
            'balancete': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['balancete'].queryset = Balancete.objects.all().order_by('nome')

