from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('about/',views.about,name="about"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path("projects/",views.projects,name="projects"),
    path("logout/",views.logout,name="logout"),
    path("add-projects/",views.add_projects,name="add-projects"),
    path("projects/updatedata/<int:id>/",views.update,name="updatedata"),
    path("projects/deletedata/<int:id>/",views.delete,name="deletedata"),

   
]