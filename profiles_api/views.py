from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


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