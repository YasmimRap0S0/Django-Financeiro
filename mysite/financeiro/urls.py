from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import IndexView, HomeView, AddReceita, CadastroView, Addbalancete, Adddespesa, BalanceteDetalhes, logout_view

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('add_receita/', AddReceita.as_view(), name='add_receita'),
    path('add_despesa/', Adddespesa.as_view(), name='add_despesa'),
    path('add_balancete/', Addbalancete.as_view(), name='add_balancete'),
    path('balancete/<int:id>/', BalanceteDetalhes.as_view(), name='balancete'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('login/', LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_view, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
