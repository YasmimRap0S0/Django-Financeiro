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
        pesquisa = request.GET.get('palavras-chave')

        balancetes = Balancete.objects.filter(usuario=usuario).order_by('-data')
        receitas = Receita.objects.filter(usuario=usuario)
        despesas = Despesa.objects.filter(usuario=usuario)
        if pesquisa:
            receitas = receitas.filter(nome__icontains=pesquisa.lower())
            despesas = despesas.filter(nome__icontains=pesquisa.lower())

        for balancete in balancetes:
            print(balancete)

        for receita in receitas:
            print(receita)

        for despesa in despesas:
            print(despesa)
       

        contexto = {'receitas': receitas, 'despesas': despesas, 'balancetes': balancetes}

        return render(request, 'financeiro/home.html', contexto)

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

    
class LoginView(View):
    def LoginUsuario(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                username = User.objects.get(email=email.lower()).username

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)

                    usuario = Usuario.objects.get(user = user) 
                    if usuario is not None:
                        return redirect('financeiro:home', usuario_id = usuario.id)
                    else:
                        
                        return redirect('financeiro:index')

                else:
                    messages.error(request, 'Email ou senha incorretos.')
        else:
            form = LoginForm()

        contexto = {
            'form': form,
        }
        return render(request, 'financeiro/login.html', contexto)



