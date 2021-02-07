from django.db import models
from django.contrib.auth.models import User

# Method choices
def user_path(instance,Filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'usuario_{0}/{1}'.format(instance.user.id, Filename)

# Create your models here.
  

class Campus(models.Model):    
   cidade = models.CharField(max_length=50, verbose_name="Cidade")
   endereco = models.CharField(max_length=150, verbose_name="Endereço")
   telefone = models.IntegerField(verbose_name="Telefone")

   def __str__(self):
       return "{}({})".format(self.cidade, self.endereco)
class Servidor(models.Model): 
    nome_completo = models.CharField(max_length=100, verbose_name="Nome") 
    siape = models.CharField(max_length=10, verbose_name="Siape")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    
    campus = models.ForeignKey(Campus, on_delete= models.PROTECT)   
    usuario = models.ForeignKey(User, on_delete= models.PROTECT)

class Status(models.Model):   
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    nome = models.CharField(max_length=50)
    def __str__(self):
       return "{} ({})".format(self.nome, self.descricao)
class Situacao(models.Model):  
     status = models.ForeignKey(Status, on_delete= models.PROTECT)
     movimentado_em = models.DateTimeField(verbose_name="Movimento-em") 
     movimentado_por = models.ForeignKey(User, on_delete= models.PROTECT) 
     detalhes = models.CharField(max_length=255, verbose_name="Detalhes", null=True, blank=True)

     def __str__(self):
        return "{} em {} por {}".format(self.status, self.movimentado_em, self.movimentado_por)
    
class Classe(models.Model):  
    nome =  models.CharField(max_length=50, verbose_name="Nome")
    nivel = models.IntegerField(verbose_name="Nível")
    descricao = models.CharField(max_length=150, verbose_name="Descrição", null=True, blank=True)
     

    def __str__(self):
       return "{} nivel {}".format(self.nome, self.nivel)            
class Progressao(models.Model):

    classe = models.ForeignKey(Classe, on_delete= models.PROTECT, verbose_name="Classe pretendida")
    data_inicio = models.DateField(verbose_name="Data de inicio")
    data_final = models.DateField(verbose_name="Data final")
    observacao = models.CharField(max_length=255, verbose_name="Observação") 
    usuario = models.ForeignKey(User, on_delete= models.PROTECT)

    

    def __str__(self):
        return "{} -> {} | {} a {}".format(self.usuario, self.classe, self.data_inicio, self.data_final)

class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name= "Descrição")

    def __str__(self):
        return "{} ({})".format(self.nome,self.descricao)

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Números")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    pontos = models.DecimalField(decimal_places=1,max_digits=4)
    detalhes = models.CharField(max_length=150, verbose_name="Detalhes")

    campo = models.ForeignKey(Campo, on_delete= models.PROTECT)

    def __str__(self):
        return "{} - {}({})".format(self.numero, self.descricao, self.campo.nome)
class Comprovante(models.Model):
    progressao = models.ForeignKey(Progressao, on_delete= models.PROTECT, verbose_name="Progressão")
    atividade = models.ForeignKey(Atividade, on_delete= models.PROTECT )
    
    quantidade = models.DecimalField(decimal_places=2,max_digits=5, verbose_name="Quantidade")
    data = models.DateField(verbose_name="Data")
    data_final = models.DateTimeField()
    arquivo = models.FileField(upload_to="pdf/" , verbose_name="Arquivo")
    
    
    usuario = models.ForeignKey(User, on_delete= models.PROTECT)

    def __str__(self):
        return "[{}] {} - {}/{}".format(self.pk, self.usuario , self.progressao, self.atividade)
        


class validacao(models.Model):
    comprovante = models.ForeignKey(Comprovante, on_delete= models.PROTECT)
    validado_em = models.DateTimeField(auto_now_add=True)
    validado_por = models.ForeignKey(User, on_delete= models.PROTECT)
    quantidade = models.DecimalField(decimal_places=2,max_digits=5 , verbose_name="Quantidade")
    justificativa = models.TextField(max_length=255, verbose_name="Justificativa")
    
    
    def __str__(self):
        return "[{}] Pontuação: {}/{} por {}".format(self.comprovante.pk, self.quantidade, self.comprovante.quantidade, self.validado_por)
    
    
   






   




