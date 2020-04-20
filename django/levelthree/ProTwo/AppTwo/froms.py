from django import forms
from AppTwo.models import User

class NewUserForm(forms.ModelForm):
#if you are using custom validation then set the fields here
#eg first_name = froms.CharField() ...
    class Meta:
        model = User
        fields = '__all__'
