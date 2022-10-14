from django.urls import path
from . import views

urlpatterns = [
    path('tag-system/', views.home_view, name="home"),
    path('post/<slug:slug>/', views.detail_view, name="detail"),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),
]
