from .models import BranchModel
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BranchSerializer
from django.db.models import Q

# Create your views here.

class BranchViewSet(viewsets.ModelViewSet):
    serializer_class = BranchSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = BranchModel.objects.all()
        city = self.request.query_params.get('city')
        alias = self.request.query_params.get('branch')
        if city is not None:
            queryset = queryset.filter(city_ru__iexact=city).filter(Q(address_ru__icontains=alias) | Q(alias__icontains=alias))[:5]
        return queryset
