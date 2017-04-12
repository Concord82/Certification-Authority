from django.contrib import admin
from .models import Cert_Parameters
from .forms import CertParamForm
# Register your models here.

class Cert_Parameters_Admin(admin.ModelAdmin):
    form = CertParamForm

admin.site.register(Cert_Parameters, Cert_Parameters_Admin)