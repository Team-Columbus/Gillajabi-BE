from django.contrib import admin
from django.urls import path, include
from users.views import SignupView, MyTokenObtainPairView, CheckIdExistView
urlpatterns = [
    path("", SignupView.as_view(), name="signup"),
    path("login/", MyTokenObtainPairView.as_view(), name="login"),
    path("id/<str:user_id>/exist/", CheckIdExistView.as_view(), name="exist-check"),
    # path('kakao/login/', KakaoLoginView.as_view(), name='kakao_login'),
    # path('kakao/callback/', KakaoCallbackView.as_view(), name='kakao_callback'),
    # path('kakao/login/finish/', KakaoLogin.as_view(), name='kakao_login_todjango'),
    # path("test/", TestApi.as_view(), name="test")
    # path("login/", LoginView.as_view(), name="login"),
]
