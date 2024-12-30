from django_filters import FilterSet
from .models import Post, UserProfile

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'hashtag': ['exact']
        }
class UserProfileFilter(FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            'nikename': ['exact']
        }