from MultipleDatabaseProject.routers.db_routers import Aqua
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import MultipleDatabaseApp
# Create your views here.

class Add(CreateView):
    model=MultipleDatabaseApp
    fields='__all__'
    template_name='add.html'
    success_url='/MultipleDatabaseApp/'
