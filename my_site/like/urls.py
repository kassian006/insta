from django.urls import path, include
from.views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'hashtag', HashtagViewSet, basename='hashtag')
router.register(r'saved',SavedViewSet, basename='saved')
router.register(r'saveitem', SaveItemViewSet, basename='saveitem')


urlpatterns = [
    path('', include(router.urls)),
    path('password_reset/verify_code/', verify_reset_code, name='verify_reset_code'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('posts/', PostListAPIView.as_view(), name = 'post_list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateAPIView.as_view(), name='post_create'),
    path('posts/create/<int:pk>/', PostEDITAPIView.as_view(), name='post_edit'),
    path('comments/', CommentListAPIView.as_view(), name= 'comment_list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment_detail'),
    path('comments/create/', CommentCreateAPIView.as_view(), name='comment_create'),
    path('comments/create/<int:pk>/', CommentEDITAPIView.as_view(), name='comment_edit'),
    path('stories/', StoryListAPIView.as_view(), name='story_list'),
    path('stories/<int:pk>/', StoryDetailAPIView.as_view(), name='story_detail'),
    path('stories/create/', StoryCreateAPIView.as_view(), name='story_create'),
    path('stories/create/<int:pk>/', StoryEDITAPIView.as_view(), name='story_edit'),
    path('follow/', FollowListAPIView.as_view(), name='follow_list'),
    path('follow/<int:pk>/', FollowDetailAPIView.as_view(), name='follow_detail'),
    path('postlike/', PostLikeListAPIView.as_view(), name='postlike_list'),
    path('postlike/<int:pk>/', PostLikeDetailAPIView.as_view(), name='postlike_detail'),
    path('commentslike/', CommentLikeListAPIView.as_view(), name='commentlike_list'),
    path('commentslike/<int:pk>/', CommentLikeDetailAPIView.as_view(), name='commentlike_detail'),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
]
