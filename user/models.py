from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	class Meta:
		db_table = 'user'
		managed = True
		verbose_name_plural = 'users'
		