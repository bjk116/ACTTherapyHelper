from django.contrib import admin

# Register your models here.
from .models import Activity, ThoughtCategory, Thought

table_to_register = [Activity, ThoughtCategory, Thought]
[admin.site.register(table) for table in table_to_register]