from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import JobApplication
from .serializers import JobApplicationSerializer
from .permissions import IsOwnerOrReadOnly

class JobApplicationListCreateView(ListCreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

     # Add filter backends here — this enables filtering, searching, ordering in this view
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields allowed for filtering via query params, e.g. ?status=pending
    filterset_fields = ['status']

    # Fields that the user can search text in, e.g. ?search=google
    search_fields = ['company', 'position']

    # Fields allowed for ordering, e.g. ?ordering=applied_date or ?ordering=-applied_date
    ordering_fields = ['applied_date']


    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return JobApplication.objects.all()

        # Return only job applications created by the currently authenticated user
        return JobApplication.objects.filter(user=user)

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
