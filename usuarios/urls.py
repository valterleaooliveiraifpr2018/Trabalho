from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate,PerfilUpdate



urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name = 'usuarios/login.html'
    ), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(), name = "logout" ),
    # path('', .as_view(), name = "" ),
    path('registrar/', UsuarioCreate.as_view(), name = "registrar"),
    
    path('atualizar/', PerfilUpdate.as_view(), name = "atualizar"),
]
