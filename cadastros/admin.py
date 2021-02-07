from django.contrib import admin


# Importar as classes
from .models import Campus, Status, Situacao, Classe, Progressao, Campo, Atividade, Comprovante
 
# Register your models here.
admin.site.register(Campus)
admin.site.register(Status)
admin.site.register(Situacao)
admin.site.register(Classe)
admin.site.register(Progressao)
admin.site.register(Campo)
admin.site.register(Atividade)
admin.site.register(Comprovante)
