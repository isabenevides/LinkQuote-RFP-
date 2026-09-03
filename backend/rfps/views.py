from rest_framework import viewsets, permissions
from .models import RFP 
from .serializers import RFPSerializer

class RFPViewSet(viewsets.ModelViewSet):
    serializer_class = RFPSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RFP.objects.filter(solicitante=self.request.user)

    def perform_create(self, serializer):
        serializer.save(solicitante=self.request.user)

