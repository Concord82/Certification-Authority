#  coding=utf-8
from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Cert_Parameters

class CertParamForm(forms.ModelForm):
    nsCertType = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Cert_Parameters.NS_CERT_TYPE)
