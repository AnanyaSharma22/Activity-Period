from django.contrib.auth import get_user_model
from rest_framework import generics
from app.models import User, ActivityPeriod
from app.serializers import UserSerializer

class getUserDetails(generics.ListAPIView):
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer 
