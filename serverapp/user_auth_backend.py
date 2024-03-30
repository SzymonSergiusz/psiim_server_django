from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from .models import Users

# TODO
class UserAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Users.objects.get(email=email)
            if user.password == check_password(password):
                return user
        except:
            return None
