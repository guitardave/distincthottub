from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.login_view, name='user_login'),
    path('logout/', views.logout_view, name='user_logout'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('new/', views.UserCreate.as_view(), name='user_new'),
    path('<int:pk>/detail/', views.UserDetail.as_view(), name='user_detail'),
    path('<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
]
