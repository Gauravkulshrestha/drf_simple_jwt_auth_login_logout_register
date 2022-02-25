from weakref import ref
from .serializers import RegsiterSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

class RegisterAPIView(APIView):
    serializer_class = RegsiterSerializer

    def post(self, request, format=None):
        serializer = RegsiterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            responce_data =  {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                }

            return Response(responce_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LogOutAPIView(APIView):

    
    def post(self, request, format=None):        
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:                   
            return Response(status=status.HTTP_400_BAD_REQUEST)