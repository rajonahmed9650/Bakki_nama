from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import SignupView,LoginView,Changeview

urlpatterns = [
    path('signup/',SignupView.as_view(),name='Signup'),
    path('login/',LoginView.as_view(),name='Login'),
    path('changepassword/',Changeview.as_view(),name='changepassword'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]