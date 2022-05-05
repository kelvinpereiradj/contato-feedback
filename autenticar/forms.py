"""
from django import forms
from django.forms import ModelForm
from django.forms import ModelForm, Textarea
from .models import *
import random



from allauth.account.forms import LoginForm
class MyCustomLoginForm(LoginForm):
    def login(self, *args, **kwargs):
        # Add your own processing here.
        # You must return the original result.
        return super().login(*args, **kwargs)


from allauth.account.forms import SignupForm
class MyCustomSignupForm(SignupForm):
    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)
        # Add your own processing here.
        # You must return the original result.
        return user


from allauth.account.forms import AddEmailForm
class MyCustomAddEmailForm(AddEmailForm):
    def save(self):
        # Ensure you call the parent class's save.
        # .save() returns an allauth.account.models.EmailAddress object.
        email_address_obj = super(MyCustomAddEmailForm, self).save()
        # Add your own processing here.
        # You must return the original result.
        return email_address_obj


from allauth.account.forms import ChangePasswordForm
class MyCustomChangePasswordForm(ChangePasswordForm):
    def save(self):
        # Ensure you call the parent class's save.
        # .save() does not return anything
        super(MyCustomChangePasswordForm, self).save()


from allauth.account.forms import SetPasswordForm
class MyCustomSetPasswordForm(SetPasswordForm):
    def save(self):
        # Ensure you call the parent class's save.
        # .save() does not return anything
        super(MyCustomSetPasswordForm, self).save()
        # Add your own processing here.


from allauth.account.forms import ResetPasswordForm
class MyCustomResetPasswordForm(ResetPasswordForm):
    def save(self):
        # Ensure you call the parent class's save.
        # .save() returns a string containing the email address supplied
        email_address = super(MyCustomResetPasswordForm, self).save()
        # Add your own processing here.
        # Ensure you return the original result
        return email_address


from allauth.account.forms import ResetPasswordKeyForm
class MyCustomResetPasswordKeyForm(ResetPasswordKeyForm):
    def save(self):
        # Add your own processing here.
        # Ensure you call the parent class's save.
        # .save() does not return anything
        super(MyCustomResetPasswordKeyForm, self).save()


from allauth.socialaccount.forms import SignupForm
class MyCustomSocialSignupForm(SignupForm):
    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSocialSignupForm, self).save(request)
        # Add your own processing here.
        # You must return the original result.
        return user


from allauth.socialaccount.forms import DisconnectForm
class MyCustomSocialDisconnectForm(DisconnectForm):
    def save(self):
        # Add your own processing here if you do need access to the
        # socialaccount being deleted.
        # Ensure you call the parent class's save.
        # .save() does not return anything
        super(MyCustomSocialDisconnectForm, self).save()
        # Add your own processing here if you don't need access to the
        # socialaccount being deleted.

"""




