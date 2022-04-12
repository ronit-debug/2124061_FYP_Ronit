from django import views
from django.urls import path
from .views import *

app_name = "prescription"
urlpatterns = [
    path("doctordashboard/", doctor_dashboard.as_view(), name="doctordashboard"),
    path("doctorlogin/", DoctorLoginView.as_view(),name="doctorlogin"),
    path("doctorlogout/", DoctorLogoutView.as_view(), name="doctorlogout"),
    path("/add-patient/", AddPatient.as_view(), name="addpatient"),
    path("/view-patient/", ViewPatient.as_view(), name="viewpatient"),
    path("manage-compare/<int:cp_id>/", ManageCompareView.as_view(), name="managecompare"),

    path("receptionistdashboard/", receptionist_dashboard.as_view(), name="receptionistdashboard"),
    path("receptionistlogin/", ReceptionistLoginView.as_view(),name="receptionistlogin"),
    path("receptionistlogout/", ReceptionistLogoutView.as_view(), name="receptionistlogout"),
    path("/add-patient-recep/", AddPatientReception.as_view(), name="recepaddpatient"),
    path("/view-patient-recep/", ViewPatientReception.as_view(), name="recepviewpatient"),
    path("manage-compare/<int:cp_id>/", RecepManageCompareView.as_view(), name="recepmanagecompare"),

    path('', Home, name='home'),
    path('about/',About, name='about'),
    path('contact/', Contact, name="contact"),
]
