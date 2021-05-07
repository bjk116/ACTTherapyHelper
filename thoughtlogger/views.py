from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """
    Initial page the user will see
    """
    return HttpResponse("Hello ACT User")