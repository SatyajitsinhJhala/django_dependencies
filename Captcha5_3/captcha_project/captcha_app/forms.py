from django import forms

class CaptchaForm(forms.Form):
    captcha_input = forms.CharField(label='Enter CAPTCHA')
