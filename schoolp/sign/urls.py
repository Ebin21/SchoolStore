from django.urls import path,include
from .  import views
app_name='sign'
urlpatterns = [
    path('',views.index, name='index'),
    path('home',views.home, name='home'),
    path('reg',views.register, name='reg'),
    path('login',views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('load_course',views.load_course, name='load_course'),
    path('register_student', views.register_student, name='register_student'),
    path('order/', views.order, name='order'),


]