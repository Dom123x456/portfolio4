from django import forms
from .models import Table

class AvailabilityForm(forms.Form):
    reservation_start = forms.DateTimeField(
        label='Reservation Start',
        widget=forms.TextInput(attrs={'type': 'datetime-local'})
    )
    reservation_end = forms.DateTimeField(
        label='Reservation End',
        widget=forms.TextInput(attrs={'type': 'datetime-local'})
    )
    table_category = forms.ModelChoiceField(
        label='Table Category',
        queryset=Table.objects.all(),
        to_field_name='category'
    )
