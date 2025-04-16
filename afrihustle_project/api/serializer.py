from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'







# Part of the functionality of the serializer is it generates/adds the id to a data while it is being stored in the database
