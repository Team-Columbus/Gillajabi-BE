from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import (
    LoginView,
    SignupView,
    MyTokenObtainPairView,
    CheckIdExistView,
    ProfileDetailView,
    UserVerifyView,
    ResetPasswordView,
    ProfileUpdateView,
    TokenValidateView,
    # KakaoCallbackView,
    # KakaoLogin,
    # KakaoLoginView
)

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    # path("login/", MyTokenObtainPairView.as_view(), name="login"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/validtate/",TokenValidateView.as_view(),name="token-validate"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("profile/", ProfileDetailView.as_view(), name="profile"),
    path("profile/", TokenValidateView.as_view(), name="profile"),
    path("profile/update/",ProfileUpdateView.as_view(),name="profile-update"),
    path("id/<str:user_id>/exist/", CheckIdExistView.as_view(), name="exist-check"),
    path("password/verify/", UserVerifyView.as_view(), name="user-verify"),
    path("password/reset/", ResetPasswordView.as_view(), name="password-reset"),
    # path('kakao/login/', KakaoLoginView.as_view(), name='kakao_login'),
    # path('kakao/callback/', KakaoCallbackView.as_view(), name='kakao_callback'),
    # path('kakao/login/finish/', KakaoLogin.as_view(), name='kakao_login_todjango'),
]
