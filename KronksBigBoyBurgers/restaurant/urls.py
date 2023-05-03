from django.urls import path
from .views import (
    ReservationFormView, ReservationListView, TableDetailView, 
    CancelReservationView, CheckoutView, register, login_view, 
    user_view, admin_view,  
)

app_name = "restaurant"

urlpatterns = [
    path("reservation-form/", ReservationFormView.as_view(), name="ReservationFormView"),
    path("reservation-list/", ReservationListView.as_view(), name="ReservationListView"),
    path("table-detail/<str:category>/", TableDetailView.as_view(), name="TableDetailView"),
    path("cancel-reservation/<int:pk>/", CancelReservationView.as_view(), name="CancelReservationView"),
    path("checkout/", CheckoutView.as_view(), name="CheckoutView"),  
]
