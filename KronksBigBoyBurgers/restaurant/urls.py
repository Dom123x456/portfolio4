from django.urls import path
from .views import (ReservationFormView, ReservationListView, TableDetailView, CancelReservationView,)

app_name = "restaurant"

urlpatterns = [
    path("reservation-form/", ReservationFormView.as_view(), name="ReservationFormView"),
    path(),
    path(),
    path(),
]