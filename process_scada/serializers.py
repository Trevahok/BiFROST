from rest_framework.serializers import ModelSerializer
from .models import Change,Diagnosis

class ChangeSerializer(ModelSerializer):
    class Meta:
        model = Change
        fields = '__all__'

class CampusSerializer(ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'