from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models

class UserManager(BaseUserManager):
    '''
    User Custom Manager
    '''
    def create_user(self, email=None, password=None):
        '''
        Create User
        '''
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        '''
        Create Superuser
        '''
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email Address', unique=True)
    is_staff = models.BooleanField('Staff member', default=False)
    is_active = models.BooleanField('Active', default=False)
    is_superuser = models.BooleanField('Is a Super user', default=False)
    create_date = models.DateTimeField('Joined Time', auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    is_app_user = models.BooleanField('App User', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name

    class Meta:
        ''' User Class Meta '''
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        app_label = 'app'
        ordering = ['name']

class ActivityPeriod(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_periods')
    start_time=models.DateTimeField(null=True, blank=True)
    end_time=models.DateTimeField(null=True, blank=True)

    class Meta:
        ''' User Class Meta '''
        verbose_name = 'Activity Period'
        verbose_name_plural = 'Activity Periods'
        app_label = 'app'
        ordering = ['user']
