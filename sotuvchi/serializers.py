from rest_framework import serializers
from .models import mashinalar

class mashinalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = mashinalar
        fields = '__all__'