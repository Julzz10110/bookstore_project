from django import forms


class OrderCreateForm(forms.Form):
    last_name = forms.CharField(label="Ntnc", max_length=50)
    first_name = forms.CharField(label="Имя", max_length=50)
    email = forms.EmailField(label="E-mail", max_length=100)
    address = forms.CharField(label="Адрес", max_length=255)
    postal_code = forms.CharField(label="Почтовый индекс", max_length=20)