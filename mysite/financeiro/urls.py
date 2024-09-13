from django.urls import path, include
from .views import IndexView, CadastroView, HomeView, LoginView

app_name = 'financeiro'

urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('home/<int:usuario_id>', HomeView.as_view(), name='home'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('login/', LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]
