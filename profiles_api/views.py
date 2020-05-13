from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from . import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer

    def get(self, request, format=None):
        apiview=['Uses http methods (get, post, patch, put, delete)',
                    'Is similar to traditional django views',
                    'Gives you the most control over the API',
                    'Is mapped manually to urls'
                ]
        return Response({'message':'hello', 'apiview':apiview})

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer

    def list(self, request):
        viewset=['Uses actions (list, create, retrieve, update, partial update)', 'and some other stuff']
        return Response({'message':'hello', 'viewset':viewset})

    def create(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!!!'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.ProfileFeedItemSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile, IsAuthenticated)
    queryset=models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)