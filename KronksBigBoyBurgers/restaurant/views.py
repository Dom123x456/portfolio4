from django.shortcuts import render
from django.views.generic import ListViews
from .models import Table, RestaurantBooking
# Create your views here.

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()

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