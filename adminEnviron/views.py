from django.shortcuts import get_object_or_404, render

from datetime import datetime
from django.views import generic
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index(request):
    """Renders the 'index' page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'adminEnviron/index.html',
        {
            'menu':'adminEnviron',
            'appname':'adminPromax',
            'title':'adminEnviron/Index',
            'year':datetime.now().year,
            'request':request,
        }
    )