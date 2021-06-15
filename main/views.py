from .models import BranchModel
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BranchSerializer

# Create your views here.

class BranchViewSet(viewsets.ModelViewSet):
    queryset = BranchModel.objects.all().order_by('city_ru')
    serializer_class = BranchSerializer
    permission_classes = [permissions.IsAuthenticated]
