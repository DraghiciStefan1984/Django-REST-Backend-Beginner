from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles import serializers

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