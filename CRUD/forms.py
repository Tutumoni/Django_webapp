from django import forms
from formExample.models import College

def validateName(name):
    pass

class CollegeForm(forms.ModelForm):
    # college_name = forms.CharField(
    #     min_length=8,
    #     max_length=20
    # )
    class Meta:
        model = College
        fields = ('college_email', 'college_address', 'college_city')
        # fields = '__all__'
        #OR
        #fields = ('college name', 'college_email')