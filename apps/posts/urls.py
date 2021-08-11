from rest_framework.routers import DefaultRouter
from apps.posts import views
from django.urls import path

router = DefaultRouter()
router.register('post', views.PostAPIViewSet, basename='posts')
router.register('image', views.PostImageAPIViewSet, basename='post_image')

urlpatterns = [
    path('like/', views.LikeCreateAPIView.as_view(), name='like'),
]

urlpatterns += router.urls
