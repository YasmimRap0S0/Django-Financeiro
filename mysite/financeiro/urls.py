from django.urls import path, include
from .views import IndexView, CadastroView, ListagemView

app_name = 'financeiro'

urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('home/', ListagemView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]
