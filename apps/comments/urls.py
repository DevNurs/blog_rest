from rest_framework.routers import DefaultRouter
from .views import CommentAPIViewSET

router = DefaultRouter()
router.register('comments', CommentAPIViewSET, basename='comments')

urlpatterns = router.urls
