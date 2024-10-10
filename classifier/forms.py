from django import forms
from django_recaptcha.fields import ReCaptchaField

class MyForm(forms.Form):
    url_input = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'id': 'url_input',
                'cols': 100,
                'rows': 5,
                'placeholder': 'Please paste your link here',
                'class': "h-full pt-3 pl-3 pr-6 md:pr-32 outline-none w-full border-2 border-light rounded-md resize-none"
            }
        ),
        required=True,
    )
    captcha = ReCaptchaField()  # Make sure this is included
