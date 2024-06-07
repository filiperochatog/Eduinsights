# urls.py

from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from usuarios.views import dicas_estudos
from . import views

urlpatterns = [
    path('dicas-de-estudo/', dicas_estudos, name='dicas_estudos'),
    path('sair/', views.sair, name = 'sair'),
    path('login/', views.login_view, name='login'),
    path('professor/home', views.professor_home, name='professor_home'),
    path('aluno/home', views.aluno_home, name='aluno_home'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('editar_perfilaluno/', views.editar_perfilaluno, name='editar_perfilaluno'),
    path('mudar_senha/', views.mudar_senha, name='mudar_senha'),
    path('mudar_senhaaluno/', views.mudar_senhaaluno, name='mudar_senhaaluno'), 
    path('simulado/2008/', views.simulado_2008, name='simulado_2008'),
    path('simulado/2010/', views.simulado_2010, name='simulado_2010'),
    path('simulado/2013/', views.simulado_2013, name='simulado_2013'),
    path('simulado/2017/', views.simulado_2017, name='simulado_2017'),
    path('simulado/2019/', views.simulado_2019, name='simulado_2019'),
    path('simulado/2099/', views.simulado_2099, name='simulado_2099'),
    path('grafico/', views.grafico2008, name='grafico2008'),
    path('grafico2011/', views.grafico2011, name='grafico2011'),
    path('grafico2014/', views.grafico2014, name='grafico2014'),
    path('grafico2017/', views.grafico2017, name='grafico2017'),
    path('grafico2019/', views.grafico2019, name='grafico2019'),
    path('grafico2099/', views.grafico2099, name='grafico2099'),
    path('prova2011/', views.prova2011, name='prova2011'),
    path('prova2014/', views.prova2014, name='prova2014'),
    path('prova2017/', views.prova2017, name='prova2017'),
    path('prova2019/', views.prova2019, name='prova2019'),
    path('prova2099/', views.prova2099, name='prova2099'),
    path('prova2008/', views.prova2008, name='prova2008'),
    
    
    
       
    
]
