from django import forms


class MultiPortForm(forms.ModelForm):
    port_base = forms.IntegerField()
    port_count = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.initial['port_base'] = self.instance.port_base
            self.initial['port_count'] = self.instance.port_count
        pass

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.port_base = self.cleaned_data['port_base']
        instance.port_count = self.cleaned_data['port_count']
        if commit:
            instance.save()
        return instance
