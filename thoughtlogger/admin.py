from django.contrib import admin

# Register your models here.
from .models import Activity, ThoughtCategory, Thought, Errands, Routines

table_to_register = [Activity, ThoughtCategory, Thought, Errands, Routines]
[admin.site.register(table) for table in table_to_register]