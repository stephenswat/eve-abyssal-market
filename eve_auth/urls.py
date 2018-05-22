from django.urls import path
from django.contrib.auth import views as auth_views

import eve_auth.views


app_name = 'eve_auth'


urlpatterns = [
    path('login/', eve_auth.views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('callback/', eve_auth.views.CallbackView.as_view(), name='callback'),
]
