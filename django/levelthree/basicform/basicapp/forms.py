from django import forms
from django.core import validators
#creating own validation
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("name needs to start with 'z'")

class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    #validating if the data is  added by bots
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
#custom validation
#clean is the keyword for custom validation clean_fieldname so that the validation is done for the fieldname specified
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOatcha bOTT")
    #     return botcatcher

    def clean(self): #clean function will aplly for whole form validation
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("email doesnot match")
