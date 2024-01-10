from django import forms
from accounts.models import User
import re
from django.forms import ValidationError
class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)


class EditProfileForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'date_of_birth', 'phone', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise ValidationError('This username is already in use. Please choose a different one.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if email:
            if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
                raise ValidationError('This email address is already associated with another account.')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # Simple phone number format validation (e.g., +1234567890)
        if phone:
            if not re.match(r'^(\+98|0)?9\d{9}$', phone):
                raise ValidationError('Please enter a valid phone number.')
        return phone

    def clean_photo(self):
        photo = self.cleaned_data['photo']
        if photo:
            # Validate file type for the photo (you can extend this based on your needs)
            main, sub = photo.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, GIF or PNG image.')
            if len(photo) > (2048 * 2048):
                raise forms.ValidationError(u'Photo size must be smaller than 4 mb')
        return photo

    def save(self, commit=True):
        # Save the form without saving the model yet
        user_instance = super().save(commit=False)

        # Handle the new photo separately if it's present in the form
        if self.cleaned_data['photo']:
            user_instance.photo = self.cleaned_data['photo']

        # Save the modified model instance with the new photo
        if commit:
            user_instance.save()