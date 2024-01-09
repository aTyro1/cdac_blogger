from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('validate',views.validate,name='validate'),
    path('register',views.register,name='register'),
    path('step1',views.step1,name='step1'),
    path('step2',views.step2,name='step2'),
    path('otplogin',views.login_otp,name='login_otp'),
    path('step1/afterLogin',views.login,name='login')
]