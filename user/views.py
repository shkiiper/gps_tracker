from django.contrib.auth import get_user_model, authenticate
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.views import View

from .models import Tracking
from .serializers import UserSerializer, TrackingSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class TokenObtainPairView(APIView):
    permission_classes = [AllowAny]

    def get_extra_actions(self):
        return []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Создайте экземпляр сериализатора и передайте пользователя для сериализации
            serializer = UserSerializer(user)
            user_data = serializer.data

            # Добавьте данные пользователя к ответу
            response_data = {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'user': user_data
            }
            return Response(response_data)
        else:
            return Response({'error': 'Invalid credentials'}, status=400)


class SaveLocationViewSet(viewsets.ModelViewSet):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.user
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        tracking = Tracking(user=user, latitude=latitude, longitude=longitude)
        tracking.save()
