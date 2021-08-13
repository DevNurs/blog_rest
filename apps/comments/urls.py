from rest_framework.routers import DefaultRouter
from apps.comments import views

router = DefaultRouter()
router.register('comments', views.CommentAPIViewSet, basename='comment')
router.register('comments_detail', views.CommentLikeDetailAPIViewSet, basename= 'detail_comment')
router.register('comments_like', views.CommentLikeCreateAPIView, basename='like_comment')

urlpatterns = router.urls
