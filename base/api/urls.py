from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes),
    path('rooms/', views.GetRooms),
    path('rooms/<str:pk>/', views.getRoom),

]