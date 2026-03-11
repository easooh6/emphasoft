from accounts.serializers.accounts import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle

class RegisterView(APIView):

    throttle_classes=[AnonRateThrottle]

    def post(self, request: Request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(RegisterSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
