from django.shortcuts import render,redirect
from usersite.models import Complaint
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import myuser
from django.contrib.auth import get_user_model
User =get_user_model()
# Create your views here.
def plogin(request):
    if request.user.is_authenticated:
        logout(request)
        # messages.error(request,'log in again')
        return redirect('phome')
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
           
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_police:
                    login(request,user)
                    return redirect('phome')
                messages.error(request,'login at the user login page')
                return redirect('home')
            messages.error(request,'invalid credantin')
            return render(request,'plogin.html')
    return render(request,'plogin.html')
def plogout(request):
     logout(request)
    #  messages.success(request,'susscesfully loged out ')
     return redirect('plogin')
@login_required     
def phome(request):
    complains= Complaint.objects.filter(city=request.user.city)
    if complains is not None:
     return render(request,'phome.html',{'complains':complains})
    else:
        messages.success(request,"no other complain")
        return render(request,'phome.html')
def found(request):
    if request.method =="POST":
        complain_id =request.POST['complain_id']
        obj = Complaint.objects.get(complain_id=complain_id)
        obj.is_found=True
        obj.save()
        messages.success(request,'sucessfully added')
        return redirect('phome')
    messages.success(request,'not entere sussfully')
    return redirect('phome')