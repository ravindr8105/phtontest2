from django.shortcuts import render
from websitekoshfin.models import person, subscription

# Create your views here.
def index(request):
    
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        messagge1=request.POST['messagge']
        ins = person(name=name1,  email=email1, messagge= messagge1)
        ins.save()
    
    
      
    
    return render(request, 'index.html')
