from django.contrib import admin
from django.urls import path,include
from .import views
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
routes = routers.DefaultRouter()
routes.register('',PostView, basename='postview'),
urlpatterns = [
   path('api/',include(routes.urls)),
   path("profile/",ProfileView.as_view()),
   path("login/", obtain_auth_token),
   path("register/", RegisterApiView.as_view()),
   path("userdataUpdate/",UserdataUpdate.as_view()),
    
]