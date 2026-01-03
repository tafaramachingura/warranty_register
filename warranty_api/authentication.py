import os
import jwt
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class tokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = request.headers.get("Authorization")

        if not auth or not auth.startswith("Bearer "):
            return None

        token = auth.split(" ", 1)[1]

        try:
            payload = jwt.decode(
                token,
                settings.SERVICE_JWT_SECRET,
                algorithms=["HS256"],
                issuer=settings.SERVICE_JWT_ISSUER,
                audience=settings.SERVICE_JWT_AUDIENCE,
            )
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError as e:
            raise AuthenticationFailed(str(e))

        issuer = payload.get("iss", "service")

        user, _ = User.objects.get_or_create(username=issuer)

        return (user, payload)
