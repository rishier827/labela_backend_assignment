from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    role = models.CharField(max_length=50, null=True, blank=True)
    groups = models.ManyToManyField(Group, blank=True, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="customuser_user_permissions")

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username