from django.core.context_processors import request
from django.utils.translation import ugettext_lazy as _

def config(request):
    return {
        'SITE_NAME': _(u'Certification Authority')
    }

def menu(request):
    return {"var": "It is my var 1 from template context processor!",
            "var2": "Second var"}