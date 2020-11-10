from django.urls import path, include
from rest_framework import routers
from filesystem.views import FileViewSet, HashViewSet

router = routers.DefaultRouter()

router.register(r'files', FileViewSet)
router.register(r'hashes', HashViewSet)

urlpatterns = [
    path('', include(router.urls))
]
