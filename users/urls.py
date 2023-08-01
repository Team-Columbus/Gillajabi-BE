from django.contrib import admin
from django.urls import path, include
from users.views import SignupView, MyTokenObtainPairView, CheckIdExistView, MyProfileView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", MyTokenObtainPairView.as_view(), name="login"),
    path("profile/", MyProfileView.as_view(), name="profile"),
    path("id/<str:user_id>/exist/", CheckIdExistView.as_view(), name="exist-check"),
    # path('kakao/login/', KakaoLoginView.as_view(), name='kakao_login'),
    # path('kakao/callback/', KakaoCallbackView.as_view(), name='kakao_callback'),
    # path('kakao/login/finish/', KakaoLogin.as_view(), name='kakao_login_todjango'),
]
