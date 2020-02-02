from django import forms
from .models import *
class TodoForm(forms.ModelForm):
     class Meta:
         model = works

         fields=['title','description','due_date','criticality','status']