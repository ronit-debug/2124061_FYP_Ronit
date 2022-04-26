from django.shortcuts import render
from msilib.schema import ListView
from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, FormView, DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.db.models import Q
# import tensorflow as tf
# from tensorflow import keras
# from keras.models import load_model
# from django.core.files.storage import FileSystemStorage
# import cv2,os
# from keras.preprocessing import image
# import numpy as np

# Create your views here.

class DoctorLoginView(FormView):
    template_name = "doctor_login.html"
    form_class = DoctorLoginView
    success_url = reverse_lazy("prescription:doctordashboard")
 
    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Doctor.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Incorrect username and password"})
 
 
        return super().form_valid(form)

#For Doctor authentication
class DoctorRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Doctor.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/doctorlogin/")
        return super().dispatch(request, *args, **kwargs)

#class of doctorhome 
class doctor_dashboard(DoctorRequiredMixin, TemplateView):
    template_name = 'doctor_home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = Patient.objects.all()
        context['patient'] = patient
        return context
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['product_list'] = Product.objects.all().order_by("-id")[:8]
    #     return context

#class for doctor logout
class DoctorLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("prescription:doctorlogin")

#For Receptionist
class ReceptionistLoginView(FormView):
    template_name = "receptionist_login.html"
    form_class = ReceptionistLoginView
    success_url = reverse_lazy("prescription:receptionistdashboard")
 
    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Receptionist.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Incorrect username and password"})
 
 
        return super().form_valid(form)

#For Receptionist authentication
class ReceptionistRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Receptionist.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/receptionistlogin/")
        return super().dispatch(request, *args, **kwargs)

#class of receptionisthome 
class receptionist_dashboard(ReceptionistRequiredMixin, TemplateView):
    template_name = 'reception_dashboard.html'

#class for receptionist logout
class ReceptionistLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("prescription:receptionistlogin")

def About(request):
     return render(request, 'about.html')

def Home(request):
     return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')

# def add_patient(request):
#     return render(request, 'add_patient.html')

# def view_patient(request):
#     return render(request, 'view_patient.html')

class AddPatient(DoctorRequiredMixin, CreateView):
    template_name = "add_patient.html"
    form_class = PatientForm
    success_url = reverse_lazy("prescription:doctordashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):

        form.save()
            
        return super().form_valid(form)

class ManageCompareView(DoctorRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        cp_id = self.kwargs["cp_id"]
        action = request.GET.get("action")
        cp_obj = Patient.objects.get(id=cp_id)
        
       
        if action == "rmv":
            
            cp_obj.delete()
           
        else:
            pass
 
        return redirect("prescription:viewpatient")

class ViewPatient(DoctorRequiredMixin, TemplateView):
    template_name = "view_patient.html"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = Patient.objects.all()
        context['patient'] = patient
        return context

class PatientDetailView(DoctorRequiredMixin, DetailView):
    template_name = "patient_detail.html"
    # model = Patient
    # context_object_name = "patient_obj"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Patient, id=id_)

class UpdatePatient(DoctorRequiredMixin, UpdateView):
    template_name = "add_patient.html"
    form_class = PatientForm
    success_url = reverse_lazy("prescription:viewpatient")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Patient, id=id_)
        
    def form_valid(self, form):

        form.save()
            
        return super().form_valid(form)


class AddPatientReception(ReceptionistRequiredMixin, CreateView):
    template_name = "add_patient_reception.html"
    form_class = PatientForm
    success_url = reverse_lazy("prescription:receptionistdashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):

        form.save()
            
        return super().form_valid(form)

class RecepManageCompareView(ReceptionistRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        cp_id = self.kwargs["cp_id"]
        action = request.GET.get("action")
        cp_obj = Patient.objects.get(id=cp_id)
        
       
        if action == "rmv":
            
            cp_obj.delete()
           
        else:
            pass
 
        return redirect("prescription:recepviewpatient")

class ViewPatientReception(ReceptionistRequiredMixin, TemplateView):
    template_name = "view_patient_reception.html"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = Patient.objects.all()
        context['patient'] = patient
        return context

# def covid_result(request):
#     if request.method == 'POST':
#         fileObj = request.FILES.get("filename", None)
#         fs=FileSystemStorage()
#         filePathName = fs.save(fileObj.name,fileObj)
#         filePathName = fs.url(filePathName)
#         model = load_model(r"D:\2124061_FYP_Ronit\covidR\covidR\AIModels\resnet_covid.h5")


#         test_image = "."+filePathName
#         print("test_image =",test_image)

#         img = cv2.imread(os.path.join(test_image))
#         print("type of image : ",type(img))
#         print("path",filePathName)
#         print(img.shape)
#         img = cv2.resize(img, (224,224))
#         img = img.reshape(1,224,224,3)
#         print(img.shape)
#         img = np.array(img, dtype='float32')

#         y_pred = model.predict(img, workers=0)
#         y_pred = np.where(y_pred>0.70, 'COVID positive','COVID negative')


#         context={
#         "filePathName":filePathName,
#         "result" : y_pred
#         }
#         return render(request,"test.html",context)
#     else:
#         return render(request,"covid-detect.html")