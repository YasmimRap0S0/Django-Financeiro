from django.views import View
from django.shortcuts import render, redirect
from .models import Usuario, User
from .forms import UsuarioForm


class IndexView(View):
    def get(self, request):
        return render(request, 'financeiro/index.html')

class HomeView(View):
    def get(self, request, usuario_id):
        # Faça algo com o usuario_id, como buscar informações no banco de dados
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

