from rest_framework import serializers
from .models import contact

class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = ['name','email','subject']