from django.urls import path
from .views import *


urlpatterns =[
        path('arse/product/', myporductview.as_view(), name='product'),
        path('arse/cart/', myCartview.as_view(), name='cart'),
        path('arse/Customer/', myCustomer.as_view(), name='Customer'),
        path('arse/catagory/',myCategoryview.as_view(),name='Category'),
        path('arse/Order/',myOrderview.as_view(),name='Order'),
        path('arse/payment/',myPaymentview.as_view(),name='payment'),
] 