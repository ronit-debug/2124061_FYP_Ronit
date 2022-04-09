from django import views
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

    path('', Home, name='home'),
    path('about/',About, name='about'),
    path('contact/', Contact, name="contact"),
    # path('/add-patient/', add_patient, name='addpatient'),
    # path('/view-patient/', view_patient, name="viewpatient"),

    path("/add-patient/", AddPatient.as_view(), name="addpatient"),
    path("/view-patient/", ViewPatient.as_view(), name="viewpatient"),
    path("manage-compare/<int:cp_id>/", ManageCompareView.as_view(), name="managecompare"),
    
]
