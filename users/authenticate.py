import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from mysettings import MY_SECRET_KEY


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except AuthenticationFailed as e:
            return None


def create_access_token(id):
    return jwt.encode(
        {
            "user_id": id,
            "exp": datetime.datetime.now() + datetime.timedelta(minutes=5),
            "iat": datetime.datetime.now(),
        },
        MY_SECRET_KEY,
        algorithm="HS256",
    )


def decode_access_token(token):
    try:
        payload = jwt.decode(token, MY_SECRET_KEY, algorithms="HS256")

        return payload["user_id"]
    except:
        raise AuthenticationFailed("unauthenticated")


def create_refresh_token(id):
    return jwt.encode(
        {
            "user_id": id,
            "exp": datetime.datetime.now() + datetime.timedelta(days=7),
            "iat": datetime.datetime.now(),
        },
        MY_SECRET_KEY,
        algorithm="HS256",
    )


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, MY_SECRET_KEY, algorithms="HS256")
        return payload["user_id"]
    except:
        raise AuthenticationFailed("unauthenticated")
