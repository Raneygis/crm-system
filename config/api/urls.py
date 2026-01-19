from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'CRM API is working!',
        'version': '1.0',
        'endpoints': {
            'auth_token': '/api/auth/token/',
            'auth_refresh': '/api/auth/token/refresh/',
            'contacts': '/api/contacts/',
            'deals': '/api/deals/',
            'tasks': '/api/tasks/',
            'users': '/api/users/',
        }
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # ВАЖНО! Вот эти строки были пропущены:
    path('contacts/', include('apps.contacts.urls')),
    path('deals/', include('apps.deals.urls')),
    path('tasks/', include('apps.tasks.urls')),
    path('users/', include('apps.users.urls')),
]
