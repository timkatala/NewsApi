from rest_framework import viewsets
from .serializers import NewsSerializer
from .models import News
from rest_framework import permissions
from .filters import NewsFilter

class NewsViewSet(viewsets.ModelViewSet):
  
    serializer_class = NewsSerializer
    permission_classes = (permissions.AllowAny,)
    filter_class = EventFilter

    def get_queryset(self):
    	return News.objects.filter(language=self.request.LANGUAGE_CODE)

    # def get_permissions(self):
    #     if self.action in ['update', 'partial_update', 'destroy', 'list']:
    #         # which is permissions.IsAdminUser 
    #         return request.user and request.user.is_staff
    #     elif self.action in ['create']:
    #         # which is permissions.IsAuthenticated
    #         return request.user and is_authenticated(request.user)             
    #     else :
    #         # which is permissions.AllowAny
    #         return True