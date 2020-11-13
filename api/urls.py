from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views
from django.urls import path 

from .views import create_user_view,token_profileview,jwt_profileview


urlpatterns = [
   path('token/login',views.obtain_auth_token),
   path('token/profile',token_profileview.as_view()),
   path('create-user',create_user_view.as_view()),
   path('jwt/login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('jwt/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
   path('jwt/profile/',jwt_profileview.as_view(), name='token-profile'),

    
]