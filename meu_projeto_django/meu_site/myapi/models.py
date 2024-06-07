from django.db import models

class UserSubmission(models.Model):
    BLOOM_TAXONOMY_CHOICES = [
        ('AN', 'Análise'),
        ('AP', 'Aplicação'),
        ('CO', 'Compreensão'),
        ('EV', 'Avaliação'),
        ('KN', 'Conhecimento'),
        ('NP', 'Não faz parte da taxonomia'),
        ('SY', 'Síntese')
    ]

    ano = models.IntegerField()
    numero = models.IntegerField()
    enunciado = models.TextField()
    images = models.ImageField(upload_to='uploads/', blank=True)
    image2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image4 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image5 = models.ImageField(upload_to='uploads/', blank=True, null=True)  # Novo campo de imagem
    image6 = models.ImageField(upload_to='uploads/', blank=True, null=True)  # Novo campo de imagem
    alternativa_a = models.CharField(max_length=500)
    alternativa_b = models.CharField(max_length=500)
    alternativa_c = models.CharField(max_length=500)
    alternativa_d = models.CharField(max_length=500)
    alternativa_e = models.CharField(max_length=500)
    resposta_correta = models.CharField(max_length=1, default='a')
    categoria_bloom = models.CharField(max_length=2, choices=BLOOM_TAXONOMY_CHOICES, default='NP')
    componentes_curriculares = models.TextField()  # Campo para entrada livre de texto
    comentario = models.TextField(blank=True, null=True)  # Novo campo de comentário
