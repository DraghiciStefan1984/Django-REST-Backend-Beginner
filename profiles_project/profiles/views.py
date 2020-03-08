from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    def get(self, request, format=None):
        apiview=['This is hello api views']
        return Response({'message':'Hello!', 'apiview':apiview})