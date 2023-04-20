from django import forms

class CreateCalculationForm(forms.Form):
    age = forms.IntegerField(label="Age", max_value=130, min_value=15)
    weight = forms.IntegerField(label="Weight", max_value=200, min_value=30)
    height = forms.IntegerField(label="Height", max_value=250, min_value=100)
    GENDER_CHOICES = [
        ('man', 'Male'),
        ('woman', 'Female'),
        ('other', 'Other')
    ]
    gender = forms.ChoiceField(label="Gender", widget=forms.RadioSelect, choices=GENDER_CHOICES)

class CreateLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", max_length=40, widget=forms.PasswordInput())

class CreateRegisterForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", max_length=40, widget=forms.PasswordInput())
    repeatPassword = forms.CharField(label="Repeat password", max_length=40, widget=forms.PasswordInput())