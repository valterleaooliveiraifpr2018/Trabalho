from django.db import models
from django.contrib.auth.models import User






# Create your models here.
class Perfil(models.Model):
    nome_completo = models.CharField(verbose_name="Nome completo", max_length=50, null=True)
    cpf = models.CharField(verbose_name="CPF", max_length=14, null=True)
    telefone = models.CharField(verbose_name="Telefone", max_length=16, null=True)

    usuario = models.OneToOneField(User, on_delete= models.CASCADE)
