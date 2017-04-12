# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from constance import config

# Create your views here.
def home(request):
    from .forms import CertForm

    if request.method == 'POST':
        cert_form = CertForm(request.POST)
        if cert_form.is_valid():
            pass
    else:
        cert_form = CertForm
    return render(request, "config.html", {'cert_form': cert_form})


def create(request):
    from .forms import CertParams

    if request.method == 'POST':
        cert_form = CertParams(request.POST)
        if cert_form.is_valid():

            #cert_form.create_dir()
            return redirect('/config')

    else:
        cert_form = CertParams
        #cert_form.capath = config.CA_PATH

    return render(request, "create.html", {'cert_form': cert_form})
