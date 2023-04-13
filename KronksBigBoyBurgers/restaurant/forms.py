from django import forms
from .models import TableCategory

class AvailabilityForm(forms.Form):
    reservation_start = forms.DateTimeField(
        label='Reservation Start',
        widget=forms.TextInput(attrs={'type': 'datetime-local'})
    )
    reservation_end = forms.DateTimeField(
        label='Reservation End',
        widget=forms.TextInput(attrs={'type': 'datetime-local'})
    )
    table_category = forms.ChoiceField(
        label='Table Category',
        choices=TableCategory.CATEGORY_CHOICES,
    )

