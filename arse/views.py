from django.shortcuts import render
from  .models import *
from  .serializers import *
from  rest_framework import generics


# Create your views here.
class myporductview(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = myproduct
class myOrderview(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = myOrder
class myCustomer(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = myCustomer
class myCartview(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = myCart
class myCategoryview(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = myCategory
class myPaymentview(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = myPayment