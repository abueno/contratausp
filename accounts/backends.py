from accounts.models import BaseUser
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model

class BaseUserModelBackend(ModelBackend):
    def authenticate(self, user_id=None, password=None, nopass=False):
        try:
            user = self.user_class.objects.get(pk=user_id)
            if user.check_password(password) or nopass:
                return user
        except self.user_class.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return self.user_class.objects.get(pk=user_id)
        except self.user_class.DoesNotExist:
            return None
    @property
    def user_class(self):
        if not hasattr(self, '_user_class'):
            self._user_class = get_model(*settings.CUSTOM_USER_MODEL.split('.', 2))
            if not self._user_class:
                raise ImproperlyConfigured('Could not get custom user model')
        return self._user_class

class UsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = BaseUser.objects.get(login=username)
            if user.check_password(password):
                return user
        except BaseUser.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return BaseUser.objects.get(pk=user_id)
        except BaseUser.DoesNotExist:
            return None
class EmailModelBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = BaseUser.objects.get(e_mail=username)
            if user.check_password(password):
                return user
        except BaseUser.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return BaseUser.objects.get(pk=user_id)
        except BaseUser.DoesNotExist:
            return None
