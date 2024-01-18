from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Complaint,feedback
from django.contrib.auth.decorators import login_required
User = get_user_model()
# Create your views here.
def index(request):
    return render(request,'index.html')
def ulogin(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method =="POST":
        username=request.POST['lusername']
        pasword=request.POST['lpassword']
        user =authenticate(request,username=username,password=pasword)
        if user is not None:
            login(request,user)
            messages.success(request,'logged in succes fully')
            return redirect('home')    
        else:
            messages.error(request,'eneter the correct deatail')
            return redirect('ulogin')

    return render(request,'ulogin.html')
def signup(request):
    if request.method =="POST":
      username =request.POST['username']
      email =request.POST['email']
      password =request.POST['password']
      password2 =request.POST['password2']
      myuser=User.objects.create_user(username,email,password)
      myuser.save()
      messages.success(request,'you are registerd succe')
      return redirect('home')
    else:
        return render(request,'signup.html')
def contact(request):
    return render(request,'contact.html')
def ulogout(request):
     logout(request)
     messages.success(request,'susscesfully loged out ')
     return redirect('home')
def creatcom(request):
    if request.method== "POST":
        complain_name =request.POST['complain_name']
        contact =request.POST['contact']
        address =request.POST['address']
        city =request.POST['city']
        vehicle_make =request.POST['vehicle_make']
        vehicle_year=request.POST['vehicle_year']
        vehicle_model =request.POST['vehicle_model']
        licence_plate =request.POST['licence_plate']
        date_of_theft =request.POST['date_of_theft']
        time_of_theft =request.POST['time_of_theft']
        location_last_seen =request.POST['location_last_seen']
        rc_no =request.POST['rc_no']
        old_vehicle_shell =request.POST['old_vehicle_shell']
        description =request.POST['description']
        user=request.user
        com=Complaint( complain_name= complain_name,contact=contact,address=address,city=city,vehicle_model=vehicle_model,licence_plate=licence_plate,date_of_theft=date_of_theft,time_of_theft=time_of_theft,location_last_seen=location_last_seen,rc_no=rc_no,old_vehicle_shell=old_vehicle_shell,description=description,user=user,vehicle_year=vehicle_year,vehicle_make=vehicle_make)
        com.save()
        messages.success(request,'complain resister succesfull')
        return redirect('home')
    return render(request,'creatcom.html')
@login_required
def viewcom(request):
    status= Complaint.objects.filter(user=request.user)
    return render(request,'viewcom.html',{'complains':status})
@login_required
def myprofile(request):
       prof= request.user
       return render(request,'myprofile.html', {'prof':prof})

def feedback1(request):
    if request.method =="POST":
       description =request.POST['description']
       user=request.user
       Feed=feedback(description=description,user=user)
       Feed.save()
       messages.success(request,'feed back send succesfully')
       return redirect('home')
    usera =request.user
    return render(request,'feedback1.html', {'usera':usera})