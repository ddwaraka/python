from django import forms
from datetime import date


class AddForm(forms.Form):
    company_code = forms.CharField(label='Company Code', max_length=100, min_length=3)
    target_price = forms.FloatField(label='Target Price')
