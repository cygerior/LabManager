from django import forms


class AddPoolForm(forms.Form):
    ip_start = forms.GenericIPAddressField()
    ip_end = forms.GenericIPAddressField()
