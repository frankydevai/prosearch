from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="products"),
    path('project/<str:pd>/', views.project, name="project")
]
