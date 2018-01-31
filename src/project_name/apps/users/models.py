from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email, is_active=True,
            is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, *args, **kwargs):
        return self._create_user(
            email, password, is_superuser=True,
            is_admin=True, *args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'email', unique=True, blank=False,
        null=False, help_text='email address')

    first_name = models.CharField('first name', max_length=50, blank=False)
    last_name = models.CharField('last name', max_length=50, blank=False)
    is_active = models.BooleanField('active', default=False)
    is_admin = models.BooleanField('admin', default=False)

    creation_date = models.DateTimeField()
    update_date = models.DateTimeField(blank=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.update_date = timezone.now()
        created = not self.pk

        if created:
            if not self.creation_date:
                self.creation_date = timezone.now()

        self.clean_fields(exclude='password')

        super().save(*args, **kwargs)

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def full_name(self):
        return self.get_full_name()

    def get_short_name(self):
        return self.first_name or self.email

    def get_full_name(self):
        if self.first_name or self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        else:
            return self.email

    def __str__(self):
        return self.email
