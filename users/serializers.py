from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    # Define password field explicitly to make it write-only (not returned in responses) 
    # Automatically handles parsing and validation of this field
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User # uses built-in User
        fields = ['username', 'email', 'password'] # parse and validate these from input

    # override create method when creating user
    def create(self, validated_data):
        # create new user
        user = User.objects.create_user(
            username=validated_data['username'],   # Get validated username
            email=validated_data.get('email', ''),  # Get validated email (default empty if not provided)
            password=validated_data['password']  # Get validated password (will be hashed)
        )
        return user