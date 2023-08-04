import requests
import json
import jwt
from datetime import datetime
from .serializers import (
    UserBaseSerializer,
    MyTokenObtainPairSerializer,
    UserInfoReturnSerializer,
    SubscribeBaseSerializer,
    CustomTokenRefreshSerializer,
)
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenRefreshView
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from .models import Subscribe

from mysettings import (
    MY_SECRET_KEY,
    MY_BASE_URL,
    MY_SOCIAL_AUTH_KAKAO_CLIENT_ID,
    MY_SOCIAL_AUTH_KAKAO_SECRET,
)
from .authenticate import CustomJWTAuthentication

User = get_user_model()
KAKAO_CALLBACK_URI = MY_BASE_URL + "api/users/kakao/callback/"


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class LoginView(APIView):
    def post(self, request):
        user_id = request.data["user_id"]
        password = request.data["password"]

        user = User.objects.filter(user_id=user_id).first()

        if user is None or not check_password(password, user.password):
            return Response(
                {"message": "아이디 또는 비밀번호가 올바르지 않습니다"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if user is not None:
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)

            response = CreateReturnInfo(user, "로그인", access_token)

            response.set_cookie("refresh_token", refresh_token, httponly=True)
            return response


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
            Subscribe.objects.create(user=user)
            return Response({"message": "회원가입 완료"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckIdExistView(APIView):
    def get(self, request, user_id):
        if user_id and User.objects.filter(user_id=user_id).exists():
            return Response({"isvalid": False}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({"isvalid": True}, status=status.HTTP_200_OK)


class UserVerifyView(APIView):
    def post(self, request):
        user_id = request.data["user_id"]
        my_birth = datetime.strptime(request.data["birth"], "%Y%m%d").date()

        user = User.objects.filter(user_id=user_id, birth=my_birth).first()

        if user:
            return Response({"isvalid": True}, status=status.HTTP_200_OK)
        else:
            return Response({"isvalid": False}, status=status.HTTP_404_NOT_FOUND)


class ResetPasswordView(APIView):
    def put(self, request):
        user_id = request.data["user_id"]
        reset_password = request.data["reset"]

        user = User.objects.get(user_id=user_id)

        if user:
            user.set_password(reset_password)
            user.save()
            return Response({"message": "변경 완료"}, status=status.HTTP_200_OK)
        return Response({"message": "유저를 찾을 수 없습니다"}, status=status.HTTP_404_NOT_FOUND)


# class KakaoLoginView(APIView):
#     def get(self, request):
#         return redirect(
#             f"https://kauth.kakao.com/oauth/authorize?client_id={MY_SOCIAL_AUTH_KAKAO_CLIENT_ID}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code&scope=account_email"
#         )


class ProfileDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user

        if user_id:
            user = User.objects.get(user_id=user_id)

            serialized_sub = SubscribeBaseSerializer(user.subscribe.all()[0]).data

            serilaizer = UserInfoReturnSerializer(user_id)
            response = CreateReturnInfo(user)
            return response
        else:
            return Response(
                {"message": "인증되지 않은 사용자입니다."}, status=status.HTTP_401_UNAUTHORIZED
            )


class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user_id = request.user

        if user_id:
            user = User.objects.get(user_id=user_id)

            edit_name = request.data["edit_name"]
            # edit_birth = datetime.strptime(request.data["edit_birth"], "%Y%m%d").date()

            user.name = edit_name
            # user.birth = edit_birth
            user.save()

            return Response({"message": "수정 완료"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "인증되지 않은 사용자입니다."}, status=status.HTTP_401_UNAUTHORIZED
            )


# class CustomTokenRefreshView(TokenRefreshView):
#     serializer_class = CustomTokenRefreshSerializer


        
class CustomTokenRefreshView(TokenRefreshView):
    def get(self, request):
        refresh_token = RefreshToken(request.COOKIES.get("refresh_token"))

        if refresh_token:
            access_token = refresh_token.access_token
            return Response({"access": str(access_token)}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "인증되지 않은 사용자입니다."}, status=status.HTTP_401_UNAUTHORIZED
            )


class TokenValidateView(APIView):
    authentication_classes = [CustomJWTAuthentication]

    def get(self, request):
        if request.user is not None and request.user.is_authenticated:
            response = CreateReturnInfo(request.user, "유효성")
            return response
        else:
            return Response(
                {"user": {}, "isvalid": False}, status=status.HTTP_401_UNAUTHORIZED
            )


def CreateReturnInfo(user, usage=None, access_token=None):
    sub_info = user.subscribe.all()[0]
    response = Response(
        {
            "user": {
                "name": user.name,
                "birth": user.birth,
                "is_subscribe": sub_info.is_subscribe,
                "sub_start": sub_info.sub_start,
                "sub_end": sub_info.sub_end,
            },
        },
        status=status.HTTP_200_OK,
    )

    if usage == "로그인":
        response.data["meesage"] = "로그인 성공"
        response.data["access_token"] = access_token
    elif usage == "유효성":
        response.data["isvalid"] = True

    return response


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

#         email = kakao_account.get("email")


#         try:

#             social_user = SocialAccount.objects.get(email=email)

#             data = {'access_token' : access_token, 'code' : code}
#             accept = requests.post(f"{MY_BASE_URL}api/users/kakao/login/finish/",data=data)
#             accept_status = accept.status_code

#             if accept_status != 200:
#                 return Response({"message" : "로그인 실패"},status= accept_status)

#             accept_json = accept.json()
#             accept_json.pop('user',None)
#             return Response(accept_json)
#         except:

#             data = {'access_token': access_token, 'code': code}
#             accept = requests.post(f"{MY_BASE_URL}api/users/kakao/login/finish/", data=data)
#             accept_status = accept.status_code

#             # 뭔가 중간에 문제가 생기면 에러
#             if accept_status != 200:
#                 return Response({"message" : "회원가입 실패"},status= accept_status)

#             accept_json = accept.json()
#             accept_json.pop('user', None)
#             return Response(accept_json)


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
