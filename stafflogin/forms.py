from django import forms
from stafflogin.models import Student, UserRegistered, PropertyOwner


class EmpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserRegistered
        fields = "__all__"


class PropertyOwnerForm(forms.ModelForm):
    class Meta:
        model = PropertyOwner
        fields = "__all__"
