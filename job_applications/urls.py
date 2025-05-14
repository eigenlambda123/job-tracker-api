from django.urls import path
from .views import JobApplicationListCreateView, JobApplicationDetailView

urlpatterns = [
    path('applications/', JobApplicationListCreateView.as_view(), name='jobapplication-list-create'),
    path('applications/<int:pk>/', JobApplicationDetailView.as_view(), name='job-application-detail'),
]
