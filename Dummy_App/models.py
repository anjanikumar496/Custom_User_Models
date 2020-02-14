from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from . import manager
from django.contrib.auth.models import User
from djutil.models import TimeStampedModel
from django.contrib.postgres.fields import ArrayField



class Employee(TimeStampedModel):    
    employee_id = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to="User/employee/profile/", max_length=700, blank=True)

    def get_full_name(self):
        parts = [self.first_name, self.middle_name, self.last_name]
        return " ".join(x for x in parts if x)

    def get_full_name_with_empid(self):
        parts = [self.first_name, self.middle_name, self.last_name]
        return " ".join(x for x in parts if x) + " (" + self.employee_id + ")"

    def __str__(self):
        return str(self.employee_id + ' => ('+self.get_full_name()+')')

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = manager.CustomUserManager()

    def save(self, *args, **kwargs):
        self.clean()
        super(User, self).save(*args, **kwargs)

    def clean(self):
        super(User, self).clean()

    @property
    def is_superuser(self):
        return self.is_staff

    @property
    def is_admin(self):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff    

    def __str__(self):
        return self.username

