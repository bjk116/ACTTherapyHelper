from django.urls import path
from . import views

app_name = 'thoughtlogger'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/errand/<int:errand_id>/', views.edit_errand, name='edit_errand'),
]