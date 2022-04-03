from django.shortcuts import render
from msilib.schema import ListView
from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, FormView, DetailView, ListView
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.db.models import Q

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
    template_name = 'receptionist_home.html'

#class for receptionist logout
class ReceptionistLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("prescription:receptionistlogin")