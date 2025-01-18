from django import forms
from django.contrib.auth.models import User

class Register(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_conf = forms.CharField(label="Confim password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')

    def pass_math(self): 
        check = self.cleaned_data
        if check['pasword'] != check['password_conf']:
            raise forms.ValidationError('Unmatching passwords!')
        return check['password_conf']

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
