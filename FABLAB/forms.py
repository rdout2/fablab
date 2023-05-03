from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields= [
            'first_name',
            'last_name',
            'email',
            'subject',
            'phone',
            'message'
        ]
        
        Widgets= {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nom'}),
            # 'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'subject': forms.TextInput(attrs={'class': 'form-control'}),
            # 'message': forms.Textarea(attrs={'class': 'form-control', 'row':1, 'cols':30}),
        }



class AdmissionForm(forms.ModelForm):
    class Meta:
        model= Admission
        fields= [
            'first_name',
            'last_name',
            'phone',
            'email',
            'cv',
            'motivation'
        ]
        
        Widgets= {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'subject': forms.TextInput(attrs={'class': 'form-control'}),
            # 'message': forms.Textarea(attrs={'class': 'form-control', 'row':1, 'cols':30}),
        }






class BlogCommentForm(forms.ModelForm):
    class Meta:
        model= BlogComment
        fields= [
            'first_name',
            'last_name',
            'email',
            'message'
        ]
        
        Widgets= {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nom'}),
            # 'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'subject': forms.TextInput(attrs={'class': 'form-control'}),
            # 'message': forms.Textarea(attrs={'class': 'form-control', 'row':1, 'cols':30}),
        }