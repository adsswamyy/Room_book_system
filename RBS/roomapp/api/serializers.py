from rest_framework.serializers import ModelSerializer
from roomapp.models import accounts
class user_registration_serializer(ModelSerializer):
    class Meta:
        model=accounts
        fields=['email','username','password','confiem_password']

