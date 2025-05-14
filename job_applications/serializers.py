from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for the JobApplication model.
    Serializes and deserializes JobApplication instances, including fields:
    'id', 'user', 'company', 'position', 'status', 'applied_date', and 'notes'.
    The 'user' field is read-only and is automatically set to the current user during creation.
    """
    class Meta:
        # uses the JobApplication model
        model = JobApplication
        # fields to serialize, deserialize
        fields = ['id', 'user', 'company', 'position', 'status', 'applied_date', 'notes']
        read_only_fields = ['user']  # Ensure the user is read-only (can't be changed)

        def create(self, validated_data):
            # Automatically add the user to the validated data
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)
