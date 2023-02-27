from django import forms

class LoginForm(forms.Form):
    text_input_attrs = {'class':'outline-none border-2 border-green-200 focus:border-green-300 p-1'}

    username = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs=text_input_attrs))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs=text_input_attrs))

class SignupForm(LoginForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs=LoginForm.text_input_attrs))
