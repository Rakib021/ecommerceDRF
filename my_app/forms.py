from django import forms
from .models import User

class registerModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','password','is_buyer','is_seller']
        

        