# UserAuth/models.py (or wherever your custom User model is defined)
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Set custom related names for groups and user_permissions
from django.contrib.auth.models import Group, Permission

Group._meta.get_field('user_set').related_name = 'custom_group_users'
Permission._meta.get_field('user_set').related_name = 'custom_permission_users'
