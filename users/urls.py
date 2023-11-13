from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.login_view, name='user_login'),
    path('logout/', views.logout_view, name='user_logout'),
    path('<int:id>/detail/', views.UserDetail.as_view(), name='user_detail'),
    path('<int:id>/update/', views.UserUpdate.as_view(), name='user_update'),
]
