from django import forms
from django.core.validators import MaxValueValidator
from .validators import validate_year

class NewForm(forms.Form):
    name = forms.CharField(label = 'name', max_length = 20)
    year = forms.IntegerField(validators = [validate_year])

    # def clean_year(self):
    #     year = self.cleaned_data.get('year')
    #     if year > 2023:
    #         raise forms.ValidationError("Year is gt 2023")
    #     return year
    #
    # def clean(self):
    #     cleaned_data = super(NewForm, self).clean()
    #     return validate_year(cleaned_data.get('year'))

