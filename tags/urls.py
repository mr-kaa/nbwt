from django.urls import path, include
from rest_framework import routers
from tags.views import TagViewSet

router = routers.DefaultRouter()

router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]
