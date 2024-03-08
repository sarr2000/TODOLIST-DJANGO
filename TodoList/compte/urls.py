from django.urls import path
from .import views
from .views import RegisterView, LoginView,logoutView



app_name ='compte'

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', logoutView,name='logout'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('userForm/', views.UserCreateview.as_view(), name='userForm'),

]
