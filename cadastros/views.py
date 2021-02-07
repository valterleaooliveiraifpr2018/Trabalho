from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Campus, Status, Situacao, Classe, Progressao, Campo, Atividade, Comprovante
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404

# Create your views here.

class CampusCreate(LoginRequiredMixin, CreateView):    
    
    login_url = reverse_lazy("login")
    model = Campus
    fields = ["cidade", "endereco", "telefone"] 
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campus')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastrar Campi"
        context["txtbotao"] = "Cadastrar"
        context["icon"] = '<i class="fa fa-check-square" aria-hidden="true"></i>'
        
        return context
class StatusCreate(LoginRequiredMixin, CreateView):   
    
    login_url = reverse_lazy("login")
    model = Status
    fields = ["nome", "descricao"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastrar Status"
        context["txtbotao"] = "Cadastrar"
        
        return context

class SituacaoCreate(LoginRequiredMixin, CreateView):    
    
    login_url = reverse_lazy("login")
    model = Situacao
    fields = ["status", "movimentado_em", "movimentado_por", "detalhes"] 
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-situacao')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastrar Situações"
        context["txtbotao"] = "Cadastrar"
        
        return context
class ClasseCreate(LoginRequiredMixin, CreateView):
    
    login_url = reverse_lazy("login")
    model = Classe
    fields = ["nome", "nivel", "descricao"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classe')   
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastrar Classes"
        context["txtbotao"] = "Cadastrar"
        
        return context
class ProgressaoCreate(LoginRequiredMixin, CreateView):
    
    login_url = reverse_lazy("login")
    model = Progressao
    fields = ["classe", "data_inicio", "data_final", "observacao"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressao')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        # antes do super o objeto não foi criado e não salvou no banco
        url = super().form_valid(form)

        # depois do super o objeto dos campos do progressao está criado antes de percistir no banco.
        # self.object.observacao += "TESTE"
        # self.object.save()

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastrar Progressões"
        context["txtbotao"] = "Cadastrar"
        
        return context
class CampoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url = reverse_lazy("login")
    model = Campo
    fields = ["nome", "descricao"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastrar Campos"
        context["txtbotao"] = "Cadastrar"
        
        return context
class AtividadeCreate(LoginRequiredMixin, CreateView):
    
    login_url = reverse_lazy("login")
    model = Atividade
    fields = ["numero", "descricao", "pontos", "detalhes", "campo"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastrar Atividades"
        context["txtbotao"] = "Cadastrar"
        
        return context
class ComprovanteCreate(LoginRequiredMixin, CreateView):    
    
    login_url = reverse_lazy("login")
    model = Comprovante
    fields = ["progressao", "atividade", "quantidade", "data", "data_final", "arquivo"]
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-comprovante')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastrar Comprovantes"
        context["txtbotao"] = "Cadastrar"
        
        return context
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url    
##################UPDATE#####################   

class CampusUpdate(LoginRequiredMixin, UpdateView):
    
    login_url = reverse_lazy("login")
    model = Campus
    fields = ["cidade", "endereco", "telefone"] 
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campus')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Campus"
        context["txtbotao"] = "Salvar"
        
        return context
class StatusUpdate(LoginRequiredMixin, UpdateView):
    
    login_url = reverse_lazy("login")
    model = Status
    fields = ["nome", "descricao"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Status"
        context["txtbotao"] = "Salvar"
        
        return context  
class SituacaoUpdate(LoginRequiredMixin, UpdateView):
    
    login_url = reverse_lazy("login")
    model = Situacao
    fields = ["status", "movimentado_em", "movimentado_por", "detalhes"] 
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-situacao')   

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Situação"
        context["txtbotao"] = "Salvar"
        
        return context 
class ClasseUpdate(LoginRequiredMixin, UpdateView):
    
    login_url = reverse_lazy("login")
    model = Classe
    fields = ["nome", "nivel", "descricao"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classe')  

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Classe"
        context["txtbotao"] = "Salvar"
        
        return context
class ProgressaoUpdate(LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy("login")
    model = Progressao
    fields = ["data_inicio", "data_final", "observacao", "usuario"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressao')

    def get_object(self, queryset=None):
        self.progressao = get_object_or_404(Progressao, pk= self.kwargs['pk'], usuario= self.request.user)
        # self.progressao = Progressao.objects.get(pk= self.kwargs['pk'], usuario= self.request.user)
        return self.progressao 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Progressão"
        context["txtbotao"] = "Salvar"
        
        return context    

class CampoUpdate(GroupRequiredMixin,LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy("login")
    model = Campo
    fields = ["nome", "descricao"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Campo"
        context["txtbotao"] = "Salvar"
        
        return context

class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    
    login_url = reverse_lazy("login")
    model = Atividade
    fields = ["numero", "descricao", "pontos", "detalhes", "campo"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Atividade"
        context["txtbotao"] = "Salvar"
        
        return context

class ComprovanteUpdate(LoginRequiredMixin, UpdateView):  
    
    login_url = reverse_lazy("login")
    model = Comprovante
    fields = ["progressao", "atividade", "quantidade", "data", "data_final", "arquivo"]
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-comprovante')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Comprovante"
        context["txtbotao"] = "Salvar"
        
        return context
       
##################DeleteViews########################################

class CampusDelete(LoginRequiredMixin, DeleteView):
    
    login_url = reverse_lazy("login")
    model = Campus
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campus')    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar Campus"
        context["txtbotao"] = "Excluir"
        
        return context
class StatusDelete(LoginRequiredMixin, DeleteView):  
    
    login_url = reverse_lazy("login")
    model = Status
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-status')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar Status"
        context["txtbotao"] = "Excluir"
        
        return context 
class SituacaoDelete(LoginRequiredMixin, DeleteView):  
    
    login_url = reverse_lazy("login")
    model = Situacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-situacao')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar Situação"
        context["txtbotao"] = "Excluir"
        
        return context
class ClasseDelete(LoginRequiredMixin, DeleteView):   
    
    login_url = reverse_lazy("login")
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-classe')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar Classe"
        context["txtbotao"] = "Excluir"
        
        return context

class ProgressaoDelete(LoginRequiredMixin, DeleteView):
    
    login_url = reverse_lazy("login")
    model = Progressao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-progressao')

    def get_object(self, queryset=None):
        self.progressao = get_object_or_404(Progressao, pk= self.kwargs['pk'], usuario= self.request.user)
        # self.progressao = Progressao.objects.get(pk= self.kwargs['pk'], usuario= self.request.user)
        return self.progressao 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar Progressão"
        context["txtbotao"] = "Excluir"
        
        return context    

class CampoDelete(LoginRequiredMixin, DeleteView):
    
    login_url = reverse_lazy("login")
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campo')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar Campo"
        context["txtbotao"] = "Excluir"
        
        return context

class AtividadeDelete(LoginRequiredMixin, DeleteView):
    
    login_url = reverse_lazy("login")
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar Atividade"
        context["txtbotao"] = "Excluir"
        
        return context

class ComprovanteDelete(LoginRequiredMixin, DeleteView):  
    
    login_url = reverse_lazy("login")
    model = Comprovante
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-comprovante')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar Comprovante"
        context["txtbotao"] = "Excluir"
        
        return context

################## LISTA ###############################################

class CampusList(LoginRequiredMixin, ListView):    
    login_url = reverse_lazy("login")
    model = Campus
    template_name = 'cadastros/lista/campus.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Campi"
        
        
        return context
class StatusList(LoginRequiredMixin, ListView):   
    login_url = reverse_lazy("login")
    model = Status
    template_name = 'cadastros/lista/status.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Status"
        
        
        return context
class SituacaoList(LoginRequiredMixin, ListView):   
    login_url = reverse_lazy("login")
    model = Situacao
    template_name = 'cadastros/lista/situacao.html' 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Situações"
        
        
        return context
class ClasseList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    model = Classe
    template_name = 'cadastros/lista/classe.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Classes"
        
        
        return context   
class ProgressaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    model = Progressao
    template_name = 'cadastros/lista/progressao.html'

    def get_queryset(self):
        self.object_list = Progressao.objects.filter(usuario = self.request.user)
    
    
        return self.object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Progressões"
        
        
        return context    

class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    model = Campo
    template_name = 'cadastros/lista/campo.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Campos"
        
        
        return context
class AtividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    model = Atividade
    template_name = 'cadastros/lista/atividade.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Atividades"
        
        
        return context
class ComprovanteList(LoginRequiredMixin, ListView):  
    login_url = reverse_lazy("login")
    model = Comprovante
    template_name = 'cadastros/lista/comprovante.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Listar Comprovantes"
        
        
        return context