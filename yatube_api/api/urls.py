from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comment')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
