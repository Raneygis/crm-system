from django.urls import path
from .views import ContactListCreateView, ContactDetailView, CompanyListCreateView, CompanyDetailView

urlpatterns = [
    path('', ContactListCreateView.as_view(), name='contact-list'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('companies/', CompanyListCreateView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
]