from django import forms
from .models.order_models import Address
class LoginForm(forms.Form):
    text_input_attrs = {'class':'outline-none border-2 border-green-200 focus:border-green-300 p-1'}

    username = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs=text_input_attrs))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs=text_input_attrs))

class SignupForm(LoginForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs=LoginForm.text_input_attrs))


class AddressForm(forms.ModelForm):

    class Meta:
        text_input_class = 'outline-none border-2 border-green-200 focus:border-green-300 p-1 '
        model = Address
        exclude = ('user',)
        widgets = {
            'name':forms.TextInput(attrs={'class':text_input_class,'placeholder':'Eg - Dhritesh kumar'}),
            'state':forms.TextInput(attrs={'class':text_input_class,'placeholder':'Eg - Bihar'}),
            'city':forms.TextInput(attrs={'class':text_input_class,'placeholder':'Eg - Purnea'}),
            'zip_code':forms.TextInput(attrs={'class':text_input_class,'placeholder':'Eg - 854301'}),
            'address_1':forms.TextInput(attrs={'class':text_input_class,'placeholder':'Eg - d block , green garder'}),
            'address_2':forms.TextInput(attrs={'class':text_input_class,'placeholder':'Eg - s block , red garden'}),
            'flat_no':forms.TextInput(attrs={'class':text_input_class,'placeholder':'Eg - A 345/4'}),
            'mobile_1':forms.TextInput(attrs={'class':text_input_class,'placeholder':'Eg - 345 345 4 345'}),
            'mobile_2':forms.TextInput(attrs={'class':text_input_class,'placeholder':'Eg - 345 345  43 45'}),
        }