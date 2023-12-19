from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Grade, Institution


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="Ismingiz", max_length=40, required=True)
    last_name = forms.CharField(label="Familiyangiz", max_length=40, required=True)
    third_name = forms.CharField(label="Otasining ismi", max_length=40, required=True)
    username = forms.CharField(label="Telefon raqam", max_length=15, required=True)
    institution = forms.ModelChoiceField(label="Maktabingiz", queryset=Institution.objects.all())
    grade = forms.ModelChoiceField(label="Sinfingiz", queryset=Grade.objects.all())
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
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
        self.fields['third_name'].widget.attrs.update({
            'name': 'third_name',
            'id': 'third_name',
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
        fields = ["first_name", "last_name", "third_name", "username", "institution", "grade", "password1", "password2"]


class ChangeInfoForm(forms.ModelForm):
    first_name = forms.CharField(label="Ismingiz", max_length=40, required=True)
    last_name = forms.CharField(label="Familiyangiz", max_length=40, required=True)
    third_name = forms.CharField(label="Otasining ismi", max_length=40, required=True)
    institution = forms.ModelChoiceField(label="Maktabingiz", queryset=Institution.objects.all())
    grade = forms.ModelChoiceField(label="Sinfingiz", queryset=Grade.objects.all())

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
        self.fields['third_name'].widget.attrs.update({
            'name': 'third_name',
            'id': 'third_name',
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
        fields = ["first_name", "last_name", "third_name", "institution", "grade"]

                
