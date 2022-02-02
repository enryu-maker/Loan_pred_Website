#Loan Pred App urls config

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='LP-home'),
    path('results', views.results, name='LP-results'),
]

