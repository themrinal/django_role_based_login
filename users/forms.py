# Import the forms module from Django
from django import forms

# Define a custom form for handling user login
class LoginForm(forms.Form):
    # A simple text input for the username field
    username = forms.CharField()
    
    # A password input field that hides characters as the user types
    password = forms.CharField(widget=forms.PasswordInput)
