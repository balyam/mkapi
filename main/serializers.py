from rest_framework import serializers
from .models import BranchModel

class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BranchModel
        fields = ['city_ru', 'address_ru', 'RezhimRabotyLeto', 'alias', 'Vyhodnye', 'RezhimRabotyZima']