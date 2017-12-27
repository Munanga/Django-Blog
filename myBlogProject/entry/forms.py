from entry.models import Entries
from django import forms


class EntryForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta():
        model = Entries
        fields = "__all__"


