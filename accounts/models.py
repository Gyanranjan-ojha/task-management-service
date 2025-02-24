from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser to add additional fields
    """
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('viewer', 'Viewer'),
    ]
    
    # Add related_name to avoid clash with auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set'  # Changed from default user_set
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set'  # Changed from default user_set
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')
    phone = models.CharField(max_length=15, blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.email

    def has_crud_permission(self):
        return self.role in ['admin', 'manager']