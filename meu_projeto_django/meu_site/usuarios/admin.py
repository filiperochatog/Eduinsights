from django.contrib import admin
from .models import Professor, Aluno
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Admin para Professor
class ProfessorInline(admin.StackedInline):
    model = Professor
    can_delete = False
    verbose_name_plural = 'professor'

# Admin para Aluno
class AlunoInline(admin.StackedInline):
    model = Aluno
    can_delete = False
    verbose_name_plural = 'alunos'

# Definindo um novo User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfessorInline, AlunoInline)

# Re-registrar UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
