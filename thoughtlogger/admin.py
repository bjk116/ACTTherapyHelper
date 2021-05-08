from django.contrib import admin

# Register your models here.
from .models import Activity, ThoughtCategory, Thought, Errands, Routines, Value, Milestone,  SelectedValue

table_to_register = [Activity, ThoughtCategory, Thought, Errands, Routines, Value, Milestone, SelectedValue]
[admin.site.register(table) for table in table_to_register]