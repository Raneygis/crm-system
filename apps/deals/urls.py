from django.urls import path
from .views import DealListCreateView, DealDetailView

urlpatterns = [
    path('', DealListCreateView.as_view(), name='deal-list'),
    path('<int:pk>/', DealDetailView.as_view(), name='deal-detail'),
]