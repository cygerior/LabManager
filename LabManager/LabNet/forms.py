from django import forms

from LabNet.models import Network, Label


class AddPoolForm(forms.Form):
    network = forms.ModelChoiceField(Network.objects.all())
    ip_start = forms.GenericIPAddressField()
    ip_end = forms.GenericIPAddressField()
    labels = forms.ModelMultipleChoiceField(Label.objects.all())
