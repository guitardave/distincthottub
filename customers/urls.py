from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('/', views.CustomerList.as_view(), name='customer_list'),
    path('new/', views.CustomerCreate.as_view(), name='customer_new')
]
