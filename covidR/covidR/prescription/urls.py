from django.urls import path
from .views import *

app_name = "prescription"
urlpatterns = [
    path("doctordashboard/", doctor_dashboard.as_view(), name="doctordashboard"),
    path("doctorlogin/", DoctorLoginView.as_view(),name="doctorlogin"),
    path("doctorlogout/", DoctorLogoutView.as_view(), name="doctorlogout"),

    path("receptionistdashboard/", receptionist_dashboard.as_view(), name="receptionistdashboard"),
    path("receptionistlogin/", ReceptionistLoginView.as_view(),name="receptionistlogin"),
    path("receptionistlogout/", ReceptionistLogoutView.as_view(), name="receptionistlogout"),

    
]
