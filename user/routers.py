from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, TokenObtainPairView, SaveLocationViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='user')
router.register(r'save-location', SaveLocationViewSet, basename='save-location')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
