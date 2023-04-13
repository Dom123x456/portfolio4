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
