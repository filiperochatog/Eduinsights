from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import EditarPerfilForm, MudarSenhaForm  
# Função de view para o login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Suponho que `professor` e `aluno` sejam atributos ou métodos que identificam o tipo do usuário.
            if hasattr(user, 'professor') and user.professor:
                return redirect('professor_home')
            elif hasattr(user, 'aluno') and user.aluno:
                return redirect('aluno_home')
            else:
                messages.error(request, "Acesso não permitido para este usuário.")
                return redirect('login')
        else:
            messages.error(request, "Nome de usuário ou senha incorretos.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Views para home  professor e aluno
@login_required(login_url='/usuarios/login/')
def professor_home(request):
    context = {'user_name': request.user.get_full_name() or request.user.username}
    return render(request, 'professor_home.html', context)

@login_required(login_url='/usuarios/login/')
def aluno_home(request):
    context = {'user_name': request.user.get_full_name() or request.user.username}
    return render(request, 'aluno_home.html', context)

# View para editar perfil
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('editar_perfil')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})

@login_required
def editar_perfilaluno(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('editar_perfilaluno')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'editar_perfilaluno.html', {'form': form})


# View para mudar senha
@login_required
def mudar_senha(request):
    if request.method == 'POST':
        form = MudarSenhaForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantém o usuário logado após a mudança de senha
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('mudar_senha')
    else:
        form = MudarSenhaForm(request.user)
    return render(request, 'mudar_senha.html', {'form': form})

@login_required
def mudar_senhaaluno(request):
    if request.method == 'POST':
        form = MudarSenhaForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantém o usuário logado após a mudança de senha
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('mudar_senhaaluno')
    else:
        form = MudarSenhaForm(request.user)
    return render(request, 'mudar_senhaaluno.html', {'form': form})


def sair(request):
    # Limpa a variável de sessão 'logado'
    request.session.flush()
    # Redireciona para a página de login
    return redirect('/usuarios/login/')


from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/usuarios/login/')
def dicas_estudos(request):
    return render(request, 'dicas_estudos.html')

@login_required(login_url='/usuarios/login/')
def simulado_2008(request):
    return render(request, 'simulado_2008.html', {})

@login_required(login_url='/usuarios/login/')
def simulado_2010(request):
    # Sua lógica para o simulado de 2010
    return render(request, 'simulado_2010.html', {})

@login_required(login_url='/usuarios/login/')
def simulado_2013(request):
    # Sua lógica para o simulado de 2013
    return render(request, 'simulado_2013.html', {})

@login_required(login_url='/usuarios/login/')
def simulado_2017(request):
    # Sua lógica para o simulado de 2017
    return render(request, 'simulado_2017.html', {})

@login_required(login_url='/usuarios/login/')
def simulado_2019(request):
    # Sua lógica para o simulado de 2019
    return render(request, 'simulado_2019.html', {})


@login_required(login_url='/usuarios/login/')
def simulado_2099(request):
    # Sua lógica para o simulado de 2019
    return render(request, 'simulado_2099.html', {})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# view prof graficos
@login_required(login_url='/usuarios/login/')
def grafico2008(request):
    return render(request, 'grafico2008.html')


@login_required(login_url='/usuarios/login/')
def grafico2011(request):
    return render(request, 'grafico2011.html')

@login_required(login_url='/usuarios/login/')
def grafico2014(request):
    return render(request, 'grafico2014.html')

@login_required(login_url='/usuarios/login/')
def grafico2017(request):
    return render(request, 'grafico2017.html')

@login_required(login_url='/usuarios/login/')
def grafico2019(request):
    return render(request, 'grafico2019.html')


@login_required(login_url='/usuarios/login/')
def grafico2099(request):
    return render(request, 'grafico2099.html')








# view alunos provas
@login_required(login_url='/usuarios/login/')
def prova2008(request):
    return render(request, 'prova2008.html')


@login_required(login_url='/usuarios/login/')
def prova2011(request):
    return render(request, 'prova2011.html')


@login_required(login_url='/usuarios/login/')
def prova2014(request):
    return render(request, 'prova2014.html')

@login_required(login_url='/usuarios/login/')
def prova2017(request):
    return render(request, 'prova2017.html')

@login_required(login_url='/usuarios/login/')
def prova2019(request):
    return render(request, 'prova2019.html')

@login_required(login_url='/usuarios/login/')
def prova2099(request):
    return render(request, 'prova2099.html')
