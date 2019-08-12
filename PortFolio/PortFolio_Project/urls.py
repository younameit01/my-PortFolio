from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path("<int:pk>/", views.Details, name='Details'),
]
