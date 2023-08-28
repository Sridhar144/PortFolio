from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    return render(request, 'main.html')    
def about(request):
    return render(request, 'about.html')    
def skills(request):
    return render(request, 'skills.html')    
def contact(request):
    if request.method=="POST":
        print("this is post")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']
        ins=Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        ins.save()
        print("The data written into the database")
    return render(request, 'contacts.html')    
