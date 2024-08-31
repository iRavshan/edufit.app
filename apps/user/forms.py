from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Grade, Institution


class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(label=_("Ismingiz"), max_length=40, required=True)
    last_name = forms.CharField(label=_("Familiyangiz"), max_length=40, required=True)
    username = forms.CharField(label=_("Telefon raqam"), max_length=15, required=True)
    institution = forms.ModelChoiceField(label=_("Maktabingiz"), queryset=Institution.objects.all())
    grade = forms.ModelChoiceField(label=_("Sinfingiz"), queryset=Grade.objects.all())
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'name': 'first_name',
            'id': 'first_name',
            'class': 'form-control'
        })
        self.fields['last_name'].widget.attrs.update({
            'name': 'last_name',
            'id': 'last_name',
            'class': 'form-control'
        })
        self.fields['username'].widget.attrs.update({
            'name': 'username',
            'id': 'username',
            'class': 'form-control'
        })
        self.fields['institution'].widget.attrs.update({
            'name': 'institution',
            'id': 'institution',
            'class': 'form-select'
        })
        self.fields['grade'].widget.attrs.update({
            'name': 'grade',
            'id': 'grade',
            'class': 'form-select'
        })
        self.fields['password1'].widget.attrs.update({
            'name': 'password1',
            'id': 'password1',
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'name': 'password2',
            'id': 'password2',
            'class': 'form-control mb-5'
        })

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "institution", "grade", "password1", "password2"]


class UserSignInForm(forms.Form):

    phone_number = forms.CharField(label=_('Telefon raqam'), 
                             required=True, 
                             widget=forms.TextInput(attrs={'id': 'phone_number',
                                                           'placeholder': _('Telefon raqam')})) 
    
    password = forms.CharField(label='Password',
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': _('Parol'),
                                                                 'id': 'password'}))


class ChangeInfoForm(forms.ModelForm):
    first_name = forms.CharField(label=_("Ismingiz"), max_length=40, required=True)
    last_name = forms.CharField(label=_("Familiyangiz"), max_length=40, required=True)
    institution = forms.ModelChoiceField(label=_("Maktabingiz"), queryset=Institution.objects.all())
    grade = forms.ModelChoiceField(label=_("Sinfingiz"), queryset=Grade.objects.all())

    def __init__(self, *args, **kwargs):
        super(ChangeInfoForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'name': 'first_name',
            'id': 'first_name',
            'class': 'form-control'
        })
        self.fields['last_name'].widget.attrs.update({
            'name': 'last_name',
            'id': 'last_name',
            'class': 'form-control'
        })
        self.fields['institution'].widget.attrs.update({
            'name': 'institution',
            'id': 'institution',
            'class': 'form-select'
        })
        self.fields['grade'].widget.attrs.update({
            'name': 'grade',
            'id': 'grade',
            'class': 'form-select'
        })

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "institution", "grade"]

                
