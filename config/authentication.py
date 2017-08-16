from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomUser:

    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return f'<PreAuthUser {self.uid}>'

    def __str__(self):
        return self.__repr__()


class HeaderAuthentication(BaseAuthentication):

    def authenticate(self, request):
        # META dict has custom headers as HTTP_{key} and capitalizes it.
        uid = request.META.get('HTTP_UID')

        if not uid:
            raise AuthenticationFailed('Missing authentication header')

        user = CustomUser(uid)

        # or something like so if you are using django.contrib.auth
        # user = User.objects.get(pk=uid)

        # or use a user microservice
        # user = requests.get(f'http://api.mydomain/users/{uid}').json()

        return (user, None)
