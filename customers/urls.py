from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.CustomerList.as_view(), name='customer_list'),
    path('new/', views.CustomerCreate.as_view(), name='customer_new'),
    path('<int:pk>/detail/', views.CustomerDetail.as_view(), name='customer_detail'),
    path('<int:pk>/update/', views.CustomerUpdate.as_view(), name='customer_update'),
    path('<int:pk>/spa/', views.create_spa, name='spa_new'),
    path('<int:id>/spa/<int:pk>/update/', views.UpdateSpa.as_view(), name='spa_update'),
]
