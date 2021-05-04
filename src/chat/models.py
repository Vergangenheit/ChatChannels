from django.db import models
from django.conf import settings
from django.db.models import Q
# Create your models here.

class ThreadManager(models.Manager):
    def by_user(self, user):
        pass
