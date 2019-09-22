from django.shortcuts import render
from roomapp.api.serializers import user_registration_serializer
from rest_framework.generics import CreateAPIView
from roomapp.models import accounts
# Create your views here.
class user_register(CreateAPIView):
    queryset = accounts.objects.all()
    serializer_class = user_registration_serializer
