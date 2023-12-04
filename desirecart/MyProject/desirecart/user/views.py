from datetime import datetime

from django.shortcuts import render
from . models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    mproduct=product.objects.all().order_by('-id')[0:4]
    return  render(request,'user/index.html',{"mixproduct":mproduct})

#############################3##

def mensproduct(request):
    a=request.GET.get('msg')
    if a==None:
        pdata=product.objects.filter(category='Mens')
    else:
        pdata=product.objects.filter(category='Mens',subcategory=a)
    scat=subcategory.objects.all().order_by('-id')
    myDict={"data":pdata,"subcat":scat}
    return  render(request,'user/mensproduct.html',myDict)

################################

def wproduct(request):
    a = request.GET.get('msg')
    if a == None:
        pdata = product.objects.filter(category='Womens')
    else:
        pdata = product.objects.filter(category='Womens', subcategory=a)
    scat = subcategory.objects.all().order_by('-id')
    myDict = {"data": pdata, "subcat": scat}
    return render(request, 'user/wproduct.html',myDict)

#################################################

def kproduct(request):
    a = request.GET.get('msg')
    if a == None:
        pdata = product.objects.filter(category='Kids')
    else:
        pdata = product.objects.filter(category='Kids', subcategory=a)
    scat = subcategory.objects.all().order_by('-id')
    myDict = {"data": pdata, "subcat": scat}
    return render(request, 'user/kproduct.html',myDict)

################################

def contactus(request):
    status=False
    if request.method=='POST':
        Name=request.POST.get("name","")
        Email=request.POST.get("email","")
        Mobile = request.POST.get("mobno","")
        Message=request.POST.get("msg","")
        res=contactinfo(name=Name,email=Email,mobno=Mobile,msg=Message)
        res.save()
        status=True
    return render(request,'user/contact.html',context={"msgs":status})

def feedback(request):
    pdata = feedbackinfo.objects.all()
    myDict = {"data1": pdata}
    status = False
    if request.method == 'POST':
        Name = request.POST.get("name", "")
        Pic = request.FILES.get("img", "")
        State = request.POST.get("state", "")
        Message = request.POST.get("msg", "")
        res = feedbackinfo(name=Name, img=Pic, state=State, msg=Message)
        res.save()
        status = True
    return render(request, 'user/feedback.html',context=myDict)


#################################################

def myorders(request):
    return  render(request,'user/myorders.html')

#################################################

def myprofile(request):
    return  render(request,'user/myprofile.html')

#################################################

def viewproduct(request):
    pid=request.GET.get('pid')
    data=product.objects.filter(id=pid)


    return  render(request,'user/viewproduct.html',{"pdata":data})

#################################################

def register(request):
    status = False
    if request.method == 'POST':
        Name = request.POST.get("name", "")
        Mobile = request.POST.get("mobile", "")
        Email = request.POST.get("email", "")
        Password = request.POST.get("password", "")
        CPassword = request.POST.get("cpassword", "")
        Pic = request.FILES.get("userpic", "")
        Address = request.POST.get("address", "")
        res = signup(name=Name,mobile=Mobile, email=Email,  password=Password,cpassword=CPassword,userpic=Pic,address=Address)
        res.save()
        #save data into users table
        myuser=User.objects.create_user(Email,Email,Password)
        myuser.first_name=Name
        myuser.last_name=Name
        myuser.save()
        status = True
    return render(request, 'user/register.html', context={"msgs": status})

##########################################################
def signin(request):
    if request.user.is_authenticated:
        page=request.GET.get('page')
        pid=request.GET.get('pid')
        username=request.user
        if page=='cart':
            sacetocart=addtocart(pid=pid,userid=username,status=True,odate=datetime.now().date())
            sacetocart.save()
        elif page=='order':
            savetoorder=order(pid=pid,userid=username,remarks="pending for admin",status=True,odatde=datetime.now().date())
            savetoorder.save()
        print('saved')
        return render(request, 'user/signin.html',context={"alreadylogin": True})
    else:
        print('not ok')
        return render(request, 'user/signin.html')
#########code to login###################################
def signin1(request):
    if request.method == 'POST':
        username = request.POST.get("uname", "")
        password = request.POST.get("password", "")
        user=auth.authenticate(username=username,password=password)
        #print(user)
        if user is not None:
            login(request,user)
            return render(request, 'user/signin.html', context={"User": True})
        else :
            return render(request, 'user/signin.html', context={"Nouser": True})
#####################################################
def logout1(request):
    logout(request)
    return render(request, 'user/index.html')

















