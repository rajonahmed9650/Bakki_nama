from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Shopkeeper


class SignupView(APIView):
    def post(self,request):
        email = request.data.get('email')
        phone = request.data.get('phone')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        shop_name = request.data.get('shop_name')


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
        
        user =  Shopkeeper.objects.create(
            email=email,
            phone=phone,
            shop_name = shop_name
        )
        user.set_password(password)
        user.save()

        return Response({"message" : "Signup Successful"})
        
