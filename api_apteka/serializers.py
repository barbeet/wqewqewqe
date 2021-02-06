from rest_framework import serializers
from general_apteka.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= '__all__'