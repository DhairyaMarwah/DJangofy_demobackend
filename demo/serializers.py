from rest_framework import serializers 
from .models import demomodal

class demomodalSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = demomodal 
        fields = '__all__' 
