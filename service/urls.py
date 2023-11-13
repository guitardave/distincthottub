from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('', views.ServiceTicketList.as_view(), name='ticket_list'),
    # path('new/', views.ServiceTicketScratch.as_view(), name='ticket_new'),
    path('<int:id>/new/', views.create_service_ticket, name='ticket_new'),
    path('<int:id>/update/<int:pk>/', views.ServiceTicketUpdate.as_view(), name='ticket_update'),
]
