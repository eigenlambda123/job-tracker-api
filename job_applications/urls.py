from django.urls import path
from .views import JobApplicationListCreateView

urlpatterns = [
    path('applications/', JobApplicationListCreateView.as_view(), name='jobapplication-list-create'),
]
