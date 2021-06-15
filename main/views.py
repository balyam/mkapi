from .models import BranchModel
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BranchSerializer
from django.db.models import Q

# Create your views here.

class BranchViewSet(viewsets.ModelViewSet):
    #queryset = BranchModel.objects.all().order_by('city_ru')
    serializer_class = BranchSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = BranchModel.objects.all()
        city = self.request.query_params.get('city')
        alias = self.request.query_params.get('branch')
        if city is not None:
            queryset = queryset.filter(city_ru__iexact=city).filter(address_ru__icontains=alias)
        return queryset
