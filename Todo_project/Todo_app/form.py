from django import forms
from .models import *
class TodoForm(forms.ModelForm):
     class Meta:
         model = work
         fields='__all__'
