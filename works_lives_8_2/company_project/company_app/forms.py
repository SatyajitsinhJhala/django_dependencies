from django import forms

class WorksForm(forms.Form):
    person_name = forms.CharField(max_length=100)
    company_name = forms.CharField(max_length=100)
    salary = forms.IntegerField()
    street = forms.CharField(max_length=200)
    city = forms.CharField(max_length=100)

class CompanySearchForm(forms.Form):
    company_name = forms.CharField(label='Company Name', max_length=100)
