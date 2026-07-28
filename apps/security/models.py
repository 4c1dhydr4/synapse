from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	# Custom User Model
	full_name = models.CharField(max_length=140, null=True)
	last_interaction = models.DateTimeField()

	def save(self, *args, **kwargs):
		if not self.last_interaction:
			self.last_interaction = timezone.now()
		self.full_name = "{} {}".format(self.first_name or '', self.last_name or '')
		return super(User, self).save(*args, **kwargs)

	@property
	def short_user(self):
		return self.username.split('@')[0]
