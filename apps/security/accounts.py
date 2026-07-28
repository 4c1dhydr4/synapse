from django.core.cache import cache
from allauth.socialaccount.models import SocialAccount
from allauth.account.auth_backends import AuthenticationBackend
from django.contrib.auth import get_user_model

class SocialAuthBackend(AuthenticationBackend):
	def get_user(self, user_id):
		cache_key = f'user_{user_id}'
		cached = cache.get(cache_key)
		if cached is not None:
			return cached

		UserModel = get_user_model()

		try:

			user = UserModel.objects.select_related(
				# related
			).prefetch_related(
				# 'groups',
			).get(id=user_id)
			cache.set(cache_key, user)

		except UserModel.DoesNotExist:
			return None

		return user

	def get_all_permissions(self, user_obj, obj=None):
		if not user_obj.is_active or user_obj.is_anonymous or obj is not None:
			return set()

		cache_key = f'user_permissions_{user_obj.pk}'

		cached = cache.get(cache_key)
		if cached is not None:
			return cached

		permissions = super().get_all_permissions(user_obj)

		cache.set(cache_key, permissions)

		return permissions
