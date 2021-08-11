from rest_framework.routers import DefaultRouter
from django.urls import path, include
from apps.comments import views

router = DefaultRouter()
router.register('comment', views.CommentAPIViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]
