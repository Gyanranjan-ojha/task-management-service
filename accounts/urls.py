from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'accounts'

urlpatterns = [
     path('register/', views.UserRegistrationView.as_view(), name='register'),
     path('login/', views.CustomLoginView.as_view(), name='login'),
     path('logout/', views.CustomLogoutView.as_view(), name='logout'),
     path('profile/', views.UserProfileUpdateView.as_view(), name='profile'),

     # Password change urls
     path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
     path('password_change/done/', 
          auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
          name='password_change_done'),

     # Password reset urls
     path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
     path('password_reset/done/',
          auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
          name='password_reset_done'),
     path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('reset/done/',
          auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
          name='password_reset_complete'),
]