from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "seller"
    # permission_classes = [IsAuthenticated]


class ProfileUpdate(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "seller"
    # permission_classes = [IsAuthenticated]
