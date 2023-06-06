from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, TokenObtainPairView

router = SimpleRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
