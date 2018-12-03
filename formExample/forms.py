from django import forms
# from django.core.validators import ValidationError

# def emailValidate(any):
#     if any.endswith('@mytectra.com') is False:
#         raise ValidationError('wrong domain nmae !')
class FormExample(forms.Form):

# tuple
    cityValues = (
        ("", "..Select an option"),
        ('1', 'Chennai'),
        ('Ban', 'Ban'),
        ('Hyd', 'Hyd'),
        ('Pun', 'Pun'),
        ('Mum', 'Mum')

    )
# radio button

    gn = (
        ('f', 'female'),
        ('m', 'male')
    )
# Checkbox

    is_active = forms.ChoiceField(widget=forms.CheckboxInput)
    is_active2 = forms.BooleanField()

    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect)
    city = forms.ChoiceField(choices=cityValues)

    username = forms.CharField(
        label='Enter Username',
        required=False,
        # min_length=6,
        max_length=10,
        error_messages={
            'min_length': 'Enter atleast 6 charaters !'
        },
        # initial='anonymous',
        widget=forms.TextInput(attrs={
            'placeholder': 'anonymous'
        })
    )

    # email = forms.EmailField(
    #     help_text='email id should end with @gmail.com !'
    #     validators=[emailValidate]
    # )

    # address = forms.CharField(
    #     widget=forms.Textarea
    # )
    password = forms.CharField(
        widget=forms.PasswordInput
    )
    confirmPassword = forms.CharField(
        widget=forms.PasswordInput
    )
    #confirmPasswordAgain = forms.CharField()
    def clean(self):
        any_variable = self.cleaned_data
        # print(any_variable)
        if 'email' in any_variable:
            if any_variable['email'].endswith('@mytectra.com') is False:
                self.errors['email'] = ['invalid domain name']
        if any_variable['password'] != any_variable['confirmPassword']:
            self.errors['confirmPassword'] = ['Password Mismatch']
        # if any_variable['password'] != any_variable['confirmPasswordAgain']:
        #     self.errors['confirmPasswordAgain'] = ['Password Mismatch']
        # if any_variable['password'] != any_variable['confirmPassword'] or any_variable['password'] != any_variable['confirmPasswordAgain']:
        #     self.errors['confirmPasswordAgain'] = ['Invalid !']

