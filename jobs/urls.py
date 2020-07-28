
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.jobdetail, name="jobdetail"),
    path('<int:job_id>/', views.jobdetail, name='jobdetail'),
    ]
