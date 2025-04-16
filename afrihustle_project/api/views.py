from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializer import UserSerializer
# We import these libraries so we can handle the logic for the api endpoints

@api_view(['GET'])
def get_user(request):
    return Response(UserSerializer({"full_name": "Lima", "age": 23}).data)

@api_view(['POST'])    # Functionality of adding user
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)