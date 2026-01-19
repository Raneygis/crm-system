from django.urls import path
from .views import UserListCreateView, UserDetailView, UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('profiles/', UserProfileListCreateView.as_view(), name='userprofile-list'),
    path('profiles/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
]
