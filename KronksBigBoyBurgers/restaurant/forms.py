from django import forms
from .models import TableCategory
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm

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
        queryset=TableCategory.objects.all(),
    )

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')



