from rest_framework import serializers

from .models import *

class myproduct(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
class myOrder(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
class myCustomer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
class myPayment(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
class myCart(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
class myCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'