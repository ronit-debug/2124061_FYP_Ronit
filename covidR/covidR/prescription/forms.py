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
                  "address", "contact", "dob", "gender", "blood", "prescription"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Full Name"
            }),
            "email": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your E-mail"
            }),
            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your Address"
            }),
            "contact": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your mobile number"
            }),
            "dob": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your date of birth"    
            }),
             "gender": forms.Select(attrs={
                "class": "form-control"    
            }),
             "blood": forms.Select(attrs={
                "class": "form-control"
               
            }),
              "prescription": forms.TextInput(attrs={
                "class": "form-control"
               
            }),
           
 
        }
