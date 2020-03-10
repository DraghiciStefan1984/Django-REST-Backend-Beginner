from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from profiles import serializers, models, permissions


# Create your views here.
class HelloApiView(APIView):
    def get(self, request, format=None):
        apiview=['This is hello api views']
        return Response({'message':'Hello!', 'apiview':apiview})

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})

    def patch(self, request, pk=None):
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    def list(self, request):
        viewset=['this is a test viewset']
        return Response({'message':'Hello', 'viewset':viewset})

    def create(self, request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
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