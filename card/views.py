from django.http import HttpResponse 
from django.shortcuts import render,redirect
from login.models import UserInfo


def carddetails(request):
    return render(request,'card-detail.html');

def login(request):
    if request.method=='POST':
        user=request.POST['email']
        password=request.POST['password']
        obj=UserInfo(email=user,password=password)
        obj.save()
        return redirect('/addentry/')
    return render(request,'login-card.html');

def balance(request):
    return render(request,'balance.html');

def Entry(request):
    item=UserInfo.objects.all()
    data={'item':item}
    return render(request,'Entry.html',data)

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
