from rest_framework import serializers
from .models import SensorGasModel

class SensorGasSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorGasModel
        fields = '__all__'