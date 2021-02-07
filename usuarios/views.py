from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .form import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Perfil



# Create your views here.


class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    # model = User
    # fields = ["username", "email", "password", ]
    success_url  = reverse_lazy("login")

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Docentes")
        
        url = super().form_valid(form)
        
        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario= self.object)
        
        return url



    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Registrar novo usuário"
        context["txtbotao"] = "Cadastrar"

        return context

class PerfilUpdate(UpdateView):
    template_name = "cadastros/form.html" 
    model = Perfil        
    fields = ["nome_completo", "cpf", "telefone", "usuario"]
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario= self.request.user)
        
        return self.object

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context["titulo"] = "Meus dados Pessoais"
        context["txtbotao"] = "Atualizar" 

        return context     
