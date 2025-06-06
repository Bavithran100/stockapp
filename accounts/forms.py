from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class StockItemForm(forms.Form):
    item_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Item Name'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    where_bought_from = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Where Bought From'}))
    quantity = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Quantity'}))
