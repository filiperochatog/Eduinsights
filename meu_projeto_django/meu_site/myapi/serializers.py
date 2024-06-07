from rest_framework import serializers
from .models import UserSubmission

class UserSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubmission
        fields = [
            'ano', 'numero', 'enunciado', 'images', 'image2', 'image3', 'image4', 'image5', 'image6',
            'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'alternativa_e',
            'resposta_correta', 'categoria_bloom', 'componentes_curriculares', 'comentario'
        ]
