from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordChangeForm

from .models import User
from .forms import UserRegistrationForm, UserProfileUpdateForm, CustomPasswordResetForm


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False  # User will be activated after email verification
        user.save()
        
        # Send verification email
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        verification_link = self.request.build_absolute_uri(
            reverse_lazy('accounts:verify_email', kwargs={'uidb64': uid, 'token': token})
        )
        
        message = render_to_string('accounts/email/verification_email.html', {
            'user': user,
            'verification_link': verification_link,
        })
        
        send_mail(
            'Verify your email',
            message,
            'noreply@taskmanager.com',
            [user.email],
            fail_silently=False,
        )
        
        messages.success(self.request, 'Please check your email to verify your account.')
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        return next_url if next_url else reverse_lazy('accounts:profile')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileUpdateForm
    template_name = 'accounts/profile_update.html'
    # Fix: Update success_url to use the correct URL name with namespace
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user


class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/email/password_reset_email.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:password_change_done')

    def form_valid(self, form):
        messages.success(self.request, 'Your password was successfully updated!')
        return super().form_valid(form)

class VerifyEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.is_email_verified = True
            user.save()
            messages.success(request, 'Your email has been verified. You can now login.')
            return redirect('accounts:login')
        else:
            messages.error(request, 'The verification link was invalid or has expired.')
            return redirect('accounts:register')