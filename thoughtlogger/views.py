from django.shortcuts import render
from django.http import HttpResponse
from .models import Errands, Routines, Thought

# Create your views here.
def index(request):
    """
    Initial page the user will see
    """
    errands = Errands.objects.order_by('-due_date')[:10]
    thoughts = Thought.objects.order_by('-create_date')[:10]
    context = {'upcoming_errands':errands, 'recent_thoughts':thoughts}
    return render(request, 'thoughtlogger/index.html', context)

def add_errand(request):
    """
    Add errand
    """
    pass

def edit_errand(request, errand_id):
    """
    Edit errand
    """
    return HttpResponse(f"Going to edit errand id {errand_id}")

def delete_errand(request):
    """
    Delete errand
    """
    pass

def add_repeating_routine(request):
    """
    Add repeating to routine
    """
    pass

def edit_repeating_routine(request):
    """
    Edit repating to routine
    """
    pass

def delete_repeating_routine(request):
    """
    Delete repeating to routine
    """
    pass

def log_present_moment_thought(requests):
    """
    Log thoughts about what they are doing in the present moment.
    """
    pass

def log_routine_thought(requests):
    """'
    Log thoughts related to daily/repeating to do items.
    """
    pass

def log_errand_thought(requests):
    """
    Log thoughts related to one-shot errands.
    """
    pass