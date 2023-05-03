from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from .models import RestaurantBooking, Table
from .forms import AvailabilityForm
from KronksBigBoyBurgers.booking_functions.availability import check_table_availability as is_table_available
from KronksBigBoyBurgers.booking_functions.availability import find_total_table_charge  # Add this import
import environ
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        # Your code to handle GET request
        return render(request, 'checkout.html')

    def post(self, request, *args, **kwargs):
        # Your code to handle POST request
        pass


class ReservationFormView(View):
    def get(self, request, *args, **kwargs):
        if "reservation_start" in request.session:
            s = request.session
            form_data = {
                "reservation_start": s['reservation_start'],
                "reservation_end": s['reservation_end'],
                "table_category": s['table_category']
            }
            form = AvailabilityForm(request.POST or None, initial=form_data)
        else:
            form = AvailabilityForm()
        return render(request, 'reservation_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            request.session['reservation_start'] = data['reservation_start'].strftime("%Y-%m-%dT%H:%M")
            request.session['reservation_end'] = data['reservation_end'].strftime("%Y-%m-%dT%H:%M")
            request.session['table_category'] = data['table_category'].category
            request.session['amount'] = find_total_table_charge(data['reservation_start'], data['reservation_end'], data['table_category'])
            return redirect('restaurant:CheckoutView')
        return HttpResponse('form not valid', form.errors)

class ReservationListView(ListView):
    model = RestaurantBooking
    template_name = "reservation_list_view.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            reservation_list = RestaurantBooking.objects.all()
            return reservation_list
        else:
            reservation_list = RestaurantBooking.objects.filter(user=self.request.user)
            return reservation_list

class TableDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        table_list = Table.objects.filter(category=category)

        if len(table_list) > 0:
            table = table_list[0]
            table_category = dict(table.TABLE_CATEGORIES).get(table.category, None)
            context = {
                'table_category': table_category,
                'form': form,
            }
            return render(request, 'table_detail_view.html', context)
        else:
            return HttpResponse('Category does not exist')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        table_list = Table.objects.filter(category=category)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_tables = []
        for table in table_list:
            if is_table_available(table, data['reservation_start'], data['reservation_end']):
                available_tables.append(table)

        if len(available_tables) > 0:
            table = available_tables[0]

            reservation = RestaurantBooking.objects.create(
                user=self.request.user,
                table=table,
                reservation_start=data['reservation_start'],
                reservation_end=data['reservation_end']
            )
            reservation.save()
            return HttpResponse(reservation)
        else:
            return HttpResponse('All tables of this category are booked! Try another one')

class CancelReservationView(DeleteView):
    model = RestaurantBooking
    template_name = 'reservation_cancel_view.html'
    success_url = reverse_lazy('restaurant:ReservationListView')



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


@user_passes_test(user_check)
def user_view(request):
    # Your user view logic here
    context = {
        "user": request.user,
        "message": "Welcome to the User Dashboard!",
    }
    return render(request, "dashboard.html", context)

@user_passes_test(admin_check)
def admin_view(request):
    # Your admin view logic here
    reservations = RestaurantBooking.objects.all()
    users = CustomUser.objects.filter(role='user')
    context = {
        "user": request.user,
        "message": "Welcome to the Admin Dashboard!",
        "reservations": reservations,
        "users": users,
    }
    return render(request, "dashboard.html", context)
