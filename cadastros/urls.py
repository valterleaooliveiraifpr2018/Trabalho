from django.urls import path
# importa as views que a gente criou
from .views import CampusCreate, StatusCreate, SituacaoCreate, ClasseCreate, ProgressaoCreate, CampoCreate, AtividadeCreate, ComprovanteCreate 
from .views import CampusUpdate, StatusUpdate, SituacaoUpdate, ClasseUpdate, ProgressaoUpdate, CampoUpdate, AtividadeUpdate, ComprovanteUpdate
from .views import CampusDelete, StatusDelete, SituacaoDelete, ClasseDelete, ProgressaoDelete, CampoDelete, AtividadeDelete, ComprovanteDelete
from .views import CampusList, StatusList, SituacaoList, ClasseList, ProgressaoList, CampoList, AtividadeList, ComprovanteList
# tem que ser URLPATTERNS porque é padrao do django
urlpatterns = [
    # todos os path tem endereço, sua_view.as_view() e o nome
    # path('endereço', MinhaView.as_view(),name='nome da url'),
    # path('', IndexView.as_view(), name=''),

    # path('', SobreView.as_view(), name=''),

    #################### ADICIONAR ############################################

    path('cadastros/campus/', CampusCreate.as_view(), name='cadastrar-campus'),
    path('cadastros/status/', StatusCreate.as_view(), name='cadastrar-status'),
    path('cadastros/situacao/', SituacaoCreate.as_view(), name='cadastrar-situacao'),
    path('cadastros/classe/', ClasseCreate.as_view(), name='cadastrar-classe'),
    path('cadastros/progressao/', ProgressaoCreate.as_view(), name='cadastrar-progressao'),
    path("cadastros/campo/", CampoCreate.as_view(), name="cadastrar-campo"),
    path("cadastros/atividade/", AtividadeCreate.as_view(), name="cadastrar-atividade"),
    path('cadastros/comprovante/', ComprovanteCreate.as_view(), name='cadastrar-comprovante'),



    
    #################### UPDATE ##############################################
    path('editar/campus/<int:pk>/', CampusUpdate.as_view(), name='editar-campus'),
    path('editar/status/<int:pk>/', StatusUpdate.as_view(), name='editar-status'),
    path('editar/situacao/<int:pk>/', SituacaoUpdate.as_view(), name='editar-situacao'),
    path('editar/classe/<int:pk>/', ClasseUpdate.as_view(), name='editar-classe'),
    path('editar/progressao/<int:pk>/', ProgressaoUpdate.as_view(), name='editar-progressao'),
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),
    path('editar/comprovante/<int:pk>/', ComprovanteUpdate.as_view(), name='editar-comprovante'),
    ################### DELETE ###############################################
    path('delete/campus/<int:pk>/', CampusDelete.as_view(), name='deletar-campus'),
    path('delete/status/<int:pk>/', StatusDelete.as_view(), name='deletar-status'),
    path('delete/situacao/<int:pk>/', SituacaoDelete.as_view(), name='deletar-situacao'),
    path('delete/classe/<int:pk>/', ClasseDelete.as_view(), name='deletar-classe'),
    path('delete/progressao/<int:pk>/', ProgressaoDelete.as_view(), name='deletar-progressao'),
    path('delete/campo/<int:pk>/', CampoDelete.as_view(), name='deletar-campo'),
    path('delete/atividade/<int:pk>/', AtividadeDelete.as_view(), name='deletar-atividade'),
    path('delete/comprovante/<int:pk>/', ComprovanteDelete.as_view(), name='deletar-comprovante'),
    ################## LISTA   ###############################################
    path('listar/campus/', CampusList.as_view(), name='listar-campus'),
    path('listar/status/', StatusList.as_view(), name='listar-status'),
    path('listar/situacoes/', SituacaoList.as_view(), name='listar-situacao'),
    path('listar/classes/', ClasseList.as_view(), name='listar-classe'),
    path('listar/progressoes/', ProgressaoList.as_view(), name='listar-progressao'),
    path('listar/campos/', CampoList.as_view(), name='listar-campo'),
    path('listar/atividades/', AtividadeList.as_view(), name='listar-atividade'),
    path('listar/comprovantes/', ComprovanteList.as_view(), name='listar-comprovante'),
]
