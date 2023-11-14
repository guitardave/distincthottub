from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('', views.ServiceTicketList.as_view(), name='ticket_list'),
    # path('new/', views.ServiceTicketScratch.as_view(), name='ticket_new'),
    path('<int:id>/new/', views.create_service_ticket, name='ticket_new'),
    path('<int:id>/update/<int:pk>/', views.update_service_ticket, name='ticket_update'),
    path('<int:id>/detail/<int:pk>/', views.ServiceTicketDetail.as_view(), name='ticket_detail'),
    path('schedule/', views.schedule_list, name='schedule_list'),
]
