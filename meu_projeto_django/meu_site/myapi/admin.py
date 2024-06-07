from django.contrib import admin
from .models import UserSubmission

class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ('ano', 'numero', 'enunciado', 'resposta_correta', 'categoria_bloom', 'componentes_curriculares')
    list_filter = ('ano', 'categoria_bloom', 'componentes_curriculares')
    search_fields = ('enunciado', 'componentes_curriculares')

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('ano', 'numero', 'enunciado')
        }),
        ('Alternativas', {
            'fields': ('alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'alternativa_e', 'resposta_correta')
        }),
        ('Multimídia', {
            'fields': ('images', 'image2', 'image3', 'image4', 'image5', 'image6')
        }),
        ('Classificação', {
            'fields': ('categoria_bloom', 'componentes_curriculares')
        }),
        ('Comentários', {
            'fields': ('comentario',)
        }),
    )

admin.site.register(UserSubmission, UserSubmissionAdmin)
