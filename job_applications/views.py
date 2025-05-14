from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import JobApplication
from .serializers import JobApplicationSerializer
from .permissions import IsOwnerOrReadOnly

class JobApplicationListCreateView(ListCreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only job applications created by the currently authenticated user
        return JobApplication.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the logged-in user with the new job application
        serializer.save(user=self.request.user)


class JobApplicationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Return only job applications created by the currently authenticated user
        return JobApplication.objects.filter(user=self.request.user)
