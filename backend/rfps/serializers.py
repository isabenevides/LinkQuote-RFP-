from rest_framework import serializers
from .models import RFP 

class RFPSerializer(serializers.ModelSerializer):
    solicitante = serializers.ReadOnlyField(source = 'solicitante.username')

    class Meta:
        model = RFP
        fields = [
            'id', 'solicitante', 'titulo', 'descricao', 'tipo_link',
            'cep', 'endereco', 'velocidade_download_mbps',
            'velocidade_upload_mbps', 'prazo_cotacao', 'criado_em' 
        ]