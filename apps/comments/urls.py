from rest_framework.routers import DefaultRouter
from apps.comments import views

router = DefaultRouter()
router.register('comments', views.CommentAPIViewSet, basename='comment')
router.register('like_for_comments', views.LikeCommentAPIViewSet, basename='like_comment')

urlpatterns = router.urls
