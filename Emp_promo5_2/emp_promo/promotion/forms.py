from django import forms
from .models import Employee

class PromotionCheckForm(forms.Form):
    emp_id = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        to_field_name='emp_id',
        label="Select Employee ID"
    )
    date_of_joining = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
        label="Date of Joining"
    )
