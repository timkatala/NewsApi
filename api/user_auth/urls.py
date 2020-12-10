from django.urls import path, include
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token, obtain_jwt_token

urlpatterns = [
    path('', obtain_jwt_token, name='token_obtain_pair'),
    path('refresh/', refresh_jwt_token),
    path('verify/', verify_jwt_token),
]