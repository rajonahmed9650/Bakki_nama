from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Shopkeeper

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = False)
    phone = serializers.CharField(required = False)
    password = serializers.CharField(write_only = True)


    def validate(self, data):
        email = data.get('email')
        phone = data.get('phone')
        passowrd = data.get('password')

        if(not email and not phone) or (email and phone):
            raise serializers.ValidationError("Provide either email or phone")
        if email:
            user = Shopkeeper.objects.filter(email=email).first()
        else:
            user = Shopkeeper.objects.filter(phone =phone).first()

        if not user:
            raise serializers.ValidationError("User not found")

        if not user.check_password(passowrd):
            raise serializers.ValidationError("Invalid password")

        refresh = RefreshToken.for_user(user)


        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            "user_id": user.id,
            "shop_name": user.shop_name
        }

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only = True)
    new_password = serializers.CharField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)

    def validate(self, data):
        user = self.context.get('request').user
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is incorrect")

        if new_password!=confirm_password:
            raise serializers.ValidationError("New password does not match")

        return data

    def save(self, **kwargs):
        user = self.context.get('request').user
        user.set_password(self._validated_data.get('new_password'))
        user.save()
        return user  




                    