from django.urls import path
from . import views

urlpatterns = [
    path("appointments/", views.AppointmentListCreates.as_view(), name="calendar"),
    path("appointments/cancel/<int:pk>", views.AppointmentDelete.as_view(),name="cancel")
]