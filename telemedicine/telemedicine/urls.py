"""telemedicine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teleapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('admindepartment', views.admindepartment, name='admindepartment'),
    path('doctor', views.doctor, name='doctor'),
    path('admindoctor', views.admindoctor, name='admindoctor'),
    path('adminapproveuser', views.adminapproveuser, name='adminapproveuser'),
    path('adminrejectuser', views.adminrejectuser, name='adminrejectuser'),
    path('adminpharmacy', views.adminpharmacy, name='adminpharmacy'),
    path('pharmacy', views.pharmacy, name='pharmacy'),
    path('courier', views.courier, name='courier'),
    path('admincourier', views.admincourier, name='admincourier'),
    path('adminmedicine', views.adminmedicine, name='adminmedicine'),
    path('pharmacyhome', views.pharmacyhome, name='pharmacyhome'),
    path('pharmacymedicine', views.pharmacymedicine, name='pharmacymedicine'),
    path('patient', views.patient, name='patient'),
    path('adminpatient', views.adminpatient, name='adminpatient'),
    path('patienthome', views.patienthome, name='patienthome'),
    path('patientrequest', views.patientrequest, name='patientrequest'),
    path('adminrequest', views.adminrequest, name='adminrequest'),
    path('adminsearchdoctor', views.adminsearchdoctor, name='adminsearchdoctor'),
    path('adminrequestallocate', views.adminrequestallocate, name='adminrequestallocate'),
    path('doctorhome', views.doctorhome, name='doctorhome'),
    path('doctorrequest', views.doctorrequest, name='doctorrequest'),
    path('doctorviewpatient', views.doctorviewpatient, name='doctorviewpatient'),
    path('doctoraddprescription', views.doctoraddprescription, name='doctoraddprescription'),
    path('doctormedicine', views.doctormedicine, name='doctormedicine'),
    path('doctorpharmacy', views.doctorpharmacy, name='doctorpharmacy'),
    path('doctorordermedicine', views.doctorordermedicine, name='doctorordermedicine'),
    path('pharmacyorder', views.pharmacyorder, name='pharmacyorder'),
    path('pharmacyorderdetails', views.pharmacyorderdetails, name='pharmacyorderdetails'),
    path('pharmacycourier', views.pharmacycourier, name='pharmacycourier'),
    path('pharmacyordercourier', views.pharmacyordercourier, name='pharmacyordercourier'),
    path('courierhome', views.courierhome, name='courierhome'),
    path('courierorder', views.courierorder, name='courierorder'),
    path('doctorfees', views.doctorfees, name='doctorfees'),
    path('pharmacyinvoice', views.pharmacyinvoice, name='pharmacyinvoice'),
    path('courierdelivery', views.courierdelivery, name='courierdelivery'),
    path('pharmacyallorder', views.pharmacyallorder, name='pharmacyallorder'),
    path('courierallorder', views.courierallorder, name='courierallorder'),
    path('patientprescription', views.patientprescription, name='patientprescription'),
    path('patientmedicine', views.patientmedicine, name='patientmedicine'),
    path('patientinvoice', views.patientinvoice, name='patientinvoice'),
    path('adminmedicinedelete', views.adminmedicinedelete, name='adminmedicinedelete'),
    path('patientfeedback', views.patientfeedback, name='patientfeedback'),
    path('adminfeedback', views.adminfeedback, name='adminfeedback'),
]
