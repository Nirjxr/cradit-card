from django.http import HttpResponse 
from django.shortcuts import render,redirect
from login.models import UserInfo
from registrationdata.models import Registaration




def carddetails(request):
    return render(request,'card-detail.html');

def MainPage(request):
    return render(request,'first-page.html')
    
def balance(request):
    return render(request,'balance.html');

def Entry(request):
    item=UserInfo.objects.all()
    data={'item':item}
    return render(request,'Entry.html',data)

def Login(request):
    if request.method=='POST':
        user=request.POST['email']
        password=request.POST['password']
        obj=UserInfo(email=user,password=password)
        obj.save()
        return redirect('/addentry/')
    return render(request,'login-card.html')


def DeletData(request,id):
    data=UserInfo.objects.get(id=id)
    data.delete()
    return redirect('/addentry/')

def EditData(request,id):
    if request.method=='POST':
        editobj=UserInfo.objects.get(id=id)
        editobj.email=request.POST['email']
        editobj.password=request.POST['password']
        editobj.save()
        return redirect('/addentry/')
    
    data=UserInfo.objects.get(id=id) 
    user={'data':data}           
    return render(request,'Edit.html',user)

def AboutUs(request):
    return render(request,'aboutus.html')


def Registartion(request):
    if request.method=='POST': 
        fname     = request.POST['fname']
        lname     = request.POST['lname']
        age       = request.POST['age']
        number    = request.POST['ccnumber']
        alt_number= request.POST['alt_number']
        email     = request.POST['email']
        country   = request.POST['country']
        password  =request.POST['ccpass']
        Objdata=Registaration(fname=fname,lname=lname,age=age,number=number,alt_number=alt_number,email=email,country=country,password=password)
        Objdata.save() 
        return redirect('/submitted-data/')
              
    return render(request,'creat-card.html')

def submitted(request):
    item=Registaration.objects.all()
    data={'item':item}
    return render(request,'Registrationentry.html',data)
