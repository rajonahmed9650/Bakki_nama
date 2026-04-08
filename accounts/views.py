from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Shopkeeper
from .serializers import LoginSerializer,ChangePasswordSerializer
from rest_framework import status,permissions


class SignupView(APIView):
    def post(self,request):
        email = request.data.get('email')
        phone = request.data.get('phone')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        shop_name = request.data.get('shop_name')
        address = request.data.get('address')


        if (not email and not phone) or (email and phone):
            return Response({
                "error":"Provide either OR phone(not both)"
            })
        if password != confirm_password:
            return Response({
                "error":"Passowrd do not match"
                })
        if email and Shopkeeper.objects.filter(email=email).exists():
            return Response({"error":"Email already exists"})
        
        if phone and Shopkeeper.objects.filter(phone=phone).exists():
            return Response({"error":"Phone already exists"})
        if not shop_name:
            return Response({"error": "Shop name required"})
        
        if not address:
            return Response({"error":"address reqired"})
        
        user =  Shopkeeper.objects.create(
            email=email,
            phone=phone,
            shop_name = shop_name,
            address = address,
        )
        user.set_password(password)
        user.save()

        return Response({"message" : "Signup Successful"})
    

class LoginView(APIView):
    # permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Changeview(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        serializer = ChangePasswordSerializer(data = request.data , context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Password changed successfully"},status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
