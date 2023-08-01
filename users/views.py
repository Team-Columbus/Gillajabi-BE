import requests
from datetime import datetime
import json
from .serializers import (
    UserBaseSerializer,
    MyTokenObtainPairSerializer,
    UserInfoReturnSerializer,
    SubscribeBaseSerializer
)
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from .models import Subscribe

from mysettings import (
    MY_BASE_URL,
    MY_SOCIAL_AUTH_KAKAO_CLIENT_ID,
    MY_SOCIAL_AUTH_KAKAO_SECRET,
)

User = get_user_model()
KAKAO_CALLBACK_URI = MY_BASE_URL + "api/users/kakao/callback/"


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class SignupView(APIView):
    def post(self, request):
        user_id = request.data["user_id"]
        password = request.data["password"]
        name = request.data["name"]
        
        my_birth = datetime.strptime(request.data["birth"], "%Y%m%d").date()
        
        request.data["birth"] = my_birth
        
        serializer = UserBaseSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.create_user(
                user_id=user_id, password=password, name=name, birth=my_birth
            )
            subscribe = Subscribe.objects.create(user=user)
            return Response({"message": "회원가입 완료"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckIdExistView(APIView):
    def get(self, request, user_id):
        if user_id and User.objects.filter(user_id=user_id).exists():
            return Response(
                {"message": "이미 사용 중인 아이디입니다"}, status=status.HTTP_409_CONFLICT
            )
        else:
            return Response({"message": "사용 가능한 아이디입니다."}, status=status.HTTP_200_OK)

class ResetPasswordView(APIView):
    pass
    # def post(self,request):
        
    #     user_id = request.data["user_id"]
    #     my_birth = datetime.strptime(request.data["birth"], "%Y%m%d").date()
    

        
# class KakaoLoginView(APIView):
#     def get(self, request):
#         return redirect(
#             f"https://kauth.kakao.com/oauth/authorize?client_id={MY_SOCIAL_AUTH_KAKAO_CLIENT_ID}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code&scope=account_email"
#         )


class MyProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        
        user_id = request.user
        user = User.objects.get(user_id=user_id)
        
        
        serialized_sub = SubscribeBaseSerializer(user.subscribe.all(),many=True).data
        
        serilaizer = UserInfoReturnSerializer(user_id)
        response_data = {
            "profile":serilaizer.data,
            "subscribe":serialized_sub
        }
        return Response(response_data, status=status.HTTP_200_OK)


# class KakaoCallbackView(APIView):
#     def get(self, request):


#         code = request.GET.get("code")

#         token_request = requests.get(
#             f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={MY_SOCIAL_AUTH_KAKAO_CLIENT_ID}&client_secret={MY_SOCIAL_AUTH_KAKAO_SECRET}&redirect_uri={KAKAO_CALLBACK_URI}&code={code}"
#         )

#         token_response_json = token_request.json()


#         access_token = token_response_json.get("access_token")
#         refresh_token = token_response_json.get("refresh_token")

#         profile_request = requests.post(
#             "https://kapi.kakao.com/v2/user/me",
#             headers={"Authorization": f"Bearer {access_token}"},
#         )

#         profile_json = profile_request.json()

#         kakao_account = profile_json.get("kakao_account")

#         # email = kakao_account.get("email", None)

#         return Response(
#             {"access": access_token, "refresh": refresh_token},
#             status=status.HTTP_200_OK,
#         )


# class KakaoLogin(SocialLoginView):
#     adapter_class = kakao_view.KakaoOAuth2Adapter
#     callback_url = KAKAO_CALLBACK_URI
#     client_class = OAuth2Client


# class TestApi(APIView):
#     permission_classes = [IsAuthenticated]
