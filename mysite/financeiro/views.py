from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Receita, Usuario, Balancete, Despesa
from django.contrib.auth import authenticate, login, logout
from .forms import UsuarioForm, AddReceitaForm, AddBalanceteForm, AddDespesaForm
from django.contrib.auth.forms import AuthenticationForm


class IndexView(View):
    def get(self, request):
        return render(request, 'financeiro/index.html')

class HomeView(View):
    def get(self, request):
        pesquisa = request.GET.get('palavras-chave')

        balancetes = Balancete.objects.all().order_by('-data')
        receitas = Receita.objects.all()
        despesas = Despesa.objects.all()
        
        if pesquisa:
            receitas = receitas.filter(nome__contains=pesquisa.lower())
            despesas = despesas.filter(nome__contains=pesquisa.lower())


        contexto = {
            'receitas': receitas,
            'despesas': despesas,
            'balancetes': balancetes
        }

        for balancete in balancetes:
            print(balancete)

        for receita in receitas:
            print(receita)

        for despesa in despesas:
            print(despesa)
       

        contexto = {'receitas': receitas, 'despesas': despesas, 'balancetes': balancetes}


        return render(request, 'financeiro/home.html', contexto)

class AddReceita(View):  
    def get(self, request):
        form = AddReceitaForm()
        return render(request, 'financeiro/add_receita.html', {'form': form})

    def post(self, request):
        form = AddReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financeiro:home')
        else:
            return render(request, 'financeiro/add_receita.html', {'form': form})
        
class Addbalancete(View):  
    def get(self, request):
        form = AddBalanceteForm()
        return render(request, 'financeiro/add_receita.html', {'form': form})

    def post(self, request):
        form = AddBalanceteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financeiro:home')
        else:
            return render(request, 'financeiro/add_receita.html', {'form': form})
        
class Adddespesa(View):  
    def get(self, request):
        form = AddDespesaForm()
        return render(request, 'financeiro/add_despesa.html', {'form': form})

    def post(self, request):
        form = AddDespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financeiro:home')
        else:
            return render(request, 'financeiro/add_despesa.html', {'form': form})

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
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                senha=form.cleaned_data['senha'],
            )

            new_usuario.save()

            return redirect('financeiro:home')

        return render(request, 'financeiro/cadastro.html', {'form': form, 'error_message': 'Ocorreu um erro ao salvar o usuário'})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'financeiro/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('financeiro:home')


        else:
            return render(request, 'financeiro/login.html', {'form': form})
