from django.shortcuts import render
from django.http import HttpResponse
from .models import destination

# Create your views here.
def index(request):
 
 #this command will go to databse and fetch data and store in dets
    dests=destination.objects.all()
    
   


    #passing dests list to index.html page 
    return render(request,'index.html', {'dests':dests})

