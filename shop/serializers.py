from rest_framework import serializers
from .models import Product, Order



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','name', 'description', 'product_image_1', 'product_image_2', 'stock_quantity', 'price', 'slug']

class OrderSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()

    class Meta:
        model = Order
        fields = fields = '__all__'
