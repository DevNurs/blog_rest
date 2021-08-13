from rest_framework.routers import DefaultRouter
from apps.posts import views
from django.urls import path

router = DefaultRouter()
router.register('post', views.PostAPIViewSet, basename='posts')
router.register('image', views.PostImageAPIViewSet, basename='post_image')
router.register('comment', views.CommentAPIView, basename='post_comment')
router.register('tag', views.TagPostView, basename='post_tag')


urlpatterns = [
    path('like/', views.LikeCreateAPIView.as_view(), name='like'),
    path('likecom/', views.CommentLIkeAPIView.as_view(), name='likecom'),
]

urlpatterns += router.urls
