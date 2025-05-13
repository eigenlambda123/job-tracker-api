from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        # uses the JobApplication model
        model = JobApplication
        # fields to serialize, deserialize
        fields = ['id', 'user', 'company', 'position', 'status', 'applied_date', 'notes']
