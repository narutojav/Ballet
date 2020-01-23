from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('udirdamj/', views.udirdamj_view, name="udirdamj"),
    path('shuugch/', views.shuugch_view, name="shuugch"),
    path('register/', views.register_view, name="register"),
    path('register_team/', views.register_team, name="team"),
    path('register_person/', views.register_person, name="person"),
]
