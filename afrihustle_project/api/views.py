from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from models import User
from .serializer import UserSerializer
# We import these libraries so we can handle the logic for the api endpoints

@api_view(('GET'))
def get_user(request):
    return Response(UserSerializer({"name": "Lima", "age": 23}))
