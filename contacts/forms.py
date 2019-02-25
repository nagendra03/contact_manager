from django import forms
from contacts.models import Contact


class NewContact(forms.ModelForm):

    class Meta:
        model = Contact
        fields = {
            'first_name',
            'middle_name',
            'last_name',
            'address',
            'email',
            'mobile',
            'alternate_mobile',
            'company',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile'}),
            'alternate_mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Alternate Mobile'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company'}),
        }


class ContactEdit(forms.ModelForm):

    class Meta:
        model = Contact
        fields = {
            'first_name',
            'middle_name',
            'last_name',
            'address',
            'email',
            'mobile',
            'alternate_mobile',
            'company',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile'}),
            'alternate_mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Alternate Mobile'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company'}),
        }
