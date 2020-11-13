from django.shortcuts import render
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin

from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .serilizers import create_user_serilizers,profile_serilizers
from authentication.models import User

class create_user_view(generics.CreateAPIView):
    serializer_class = create_user_serilizers

class token_profileview(ListModelMixin,generics.GenericAPIView):
    uthentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = None
    serializer_class =profile_serilizers
    

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        user=self.request.user
        self.queryset = User.objects.filter(email = user)
        return self.queryset

class jwt_profileview(ListModelMixin,generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = None
    serializer_class =profile_serilizers
    

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        user=self.request.user
        self.queryset = User.objects.filter(email = user)
        return self.queryset

