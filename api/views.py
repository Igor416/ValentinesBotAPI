from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from .serializers import UserSerializer, LetterSerializer
from .models import User, Letter

# Create your views here.
class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailedView(RetrieveAPIView):
    lookup_url_kwarg = 'username'
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        return Response(UserSerializer(User.objects.get(username=self.kwargs.get('username'))).data)

class UserFullNameView(ListAPIView):
    lookup_url_kwarg = 'full_name'
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        def get_names(full_name):
            names = [full_name, ' '.join(full_name.split(' ')[::-1])]
            names += [name.lower() for name in names] + [name.title() for name in names]
            return list(set(names))
        return User.objects.filter(full_name__in=get_names(self.kwargs.get('full_name')))

class LetterView(ListCreateAPIView):
    lookup_url_kwarg = 'reciever'
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

    def get_queryset(self, *args, **kwargs):
        return Letter.objects.filter(receiver=self.kwargs.get('receiver'))