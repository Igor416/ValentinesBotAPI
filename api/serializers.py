from rest_framework.serializers import ModelSerializer
from .models import User, Letter

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LetterSerializer(ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'