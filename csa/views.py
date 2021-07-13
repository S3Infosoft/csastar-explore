from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from . models import Companies


# Create your views here.
def home(request):
    results=Companies.objects.all()

    return render(request, 'home.html', {'data':results})
