from django import forms

from events.models import Event


class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['id', 'user', 'level', 'environment', 'address', 'log', 'archive']

