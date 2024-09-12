from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
#from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Receita, Usuario, Balancete, Despesa
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UsuarioForm ,  LoginForm

class IndexView(View):
    def get(self, request):
        return render(request, 'financeiro/index.html')

class HomeView(View):
    def get(self, request, usuario_id):

        usuario = Usuario.objects.get(id=usuario_id)
        return render(request, 'financeiro/home.html', {'usuario': usuario})

class CadastroView(View):
    def get(self, request):
        form = UsuarioForm()
        return render(request, 'financeiro/cadastro.html', {'form': form})

    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            novo_usuario = User.objects.create_user(
                username=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['senha'],
            )

            new_usuario = Usuario(
                 user=novo_usuario,
                 nome=form.cleaned_data['nome'], ##inserir na tabela usuario
                 email=form.cleaned_data['email'],
                 senha=form.cleaned_data['senha'],
                 )

            new_usuario.save()

            usuario_id = new_usuario.id

            return redirect('financeiro:home', usuario_id=usuario_id)

        return render(request,'financeiro/cadastro.html', {'form': form, 'error_message': 'Ocorreu um erro ao salvar o usuário'})

class ListagemView(View):
    def get(self, request):
        
        pesquisa = request.GET.get('palavras-chave')

        receitas = Receita.objects.all()
        despesas = Despesa.objects.all()
        if pesquisa:
            receitas = receitas.filter(nome__icontains=pesquisa.lower())
            despesas = despesas.filter(nome__icontains=pesquisa.lower())
            
        balancetes = Balancete.objects.order_by('-data')
    
        
        for balancete in balancetes:
            print(balancete.nome)  
        for receita in receitas:
            print(receita.nome)
        context = {'receitas': receitas, 'balancetes': balancetes}

        return render(request, 'financeiro/home.html', context)
    
class UsuarioView(View):
    def LoginUsuario(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                # BUGFIX: Usuário não existente não está sendo tratado.
                username = User.objects.get(email=email.lower()).username

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)

                    usuario_login = Usuario.objects.get(user = user) ## assume que o usuário é programador
                    if usuario_login is not None:
                        return redirect('financeiro:home', usuario_id=user.id)

                else:
                    messages.error(request, 'Email ou senha incorretos.')
        else:
            form = LoginForm()

        contexto = {
            'form': form,

        }
        return render(request, 'financeiro/login.html', contexto)



