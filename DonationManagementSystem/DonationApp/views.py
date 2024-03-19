from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request,"index.html") 

def all_logins(request):
    return render(request,"all_logins.html") 

def donor_signup(request):
  
    if request.method == "POST":
        name1=request.POST.get("name")
        contact1=request.POST.get("contact")
        email1=request.POST.get('email')
        password1=request.POST.get("pass1")
        donorpic1=request.FILES.get("donorpic")
        address1=request.POST.get("address")

        try:
            user=User.objects.create_user(username=email1, password=password1,)
            Donor.objects.create( user=user,name=name1,contact=contact1,email=email1,password=password1,donorpic=donorpic1,address=address1)
            error="no"
        except:
             error="yes"    
    return render(request,"donor_signup.html",locals())

def donor_login(request):
    if request.method == "POST":
        email1=request.POST.get("email")
        password1=request.POST.get("password")
        donor = authenticate(request,username=email1,password=password1)
        if Donor:
            login(request,donor)
            error="no"
        else:
            error="yes"
    return render(request,"donor_login.html",locals())    



def donor_reset(request):
    return render(request,"donor_reset.html")
    
def donor_home(request):
    if not request.user.is_authenticated:
        return redirect("donor_login")
    return render(request,"donor_home.html")

def donate_now(request):

        if request.method == "POST":
            donorname1=request.POST.get("donorname")
            donationname1=request.POST.get("donationname")
            donationpic1=request.FILES.get("donationpic")
            collectionloc1=request.POST.get('collectionloc')
            description1=request.POST.get("description")
           
            try:
                Donation.objects.create(donorname=donorname1,donationname=donationname1,donationpic=donationpic1,description=description1,status="pending")
                error= "no"
            except:
                error= "yes" 
        return render(request,"donate_now.html",locals())

def logout_donor(request):
    logout(request)
    return redirect ("index.")

def donation_history(request):
    # user=request.user
    #  donor=Donor.objects.get(user=user)
    # donation=Donation.objects.filter(donor=donor)
    return render(request,"donation_history.html",locals())

def footer(request):
    return render(request,"footer.html")

def admin_login(request):
        if request.method == "POST":
            username1=request.POST.get("username")
            password1=request.POST.get("password")
            User = authenticate(username=username1,password=password1)
      
            if User.is_staff:
                login(request,User)
                error="no"
            else:
                 error="yes"
        return render(request,"admin_login.html",locals())


def admin_home(request):
    if not request.user.is_authenticated:
      return redirect("admin_login")
    return render(request,"admin_home.html")

def volunteer_login(request):

    return render(request,"volunteer_login.html")


