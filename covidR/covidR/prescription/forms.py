from django import forms
from .models import *
class DoctorLoginView(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class ReceptionistLoginView(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "email",
                  "address", "contact", "dob", "gender", "blood"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Order By"
            }),
            "email": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your Shipping Address"
            }),
            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your Mobile Number"
            }),
            "contact": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email"
            }),
            "dob": forms.TextInput(attrs={
                "class": "form-control"
               
            }),
             "gender": forms.Select(attrs={
                "class": "form-control"
               
            }),
             "blood": forms.Select(attrs={
                "class": "form-control"
               
            }),
           
 
        }
