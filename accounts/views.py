from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

def login_view(request):
    if request.method == 'POST' :
        username = request.POST.get("username")
        password =  request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        print(username,password)
        if user is None:
            context={"error": "invalid username or password"}
            return render(request,"accounts/login.html",context)
        login(request,user)
        return redirect('/')
    return render(request,'accounts/login.html',context={})


def register_view(request):

    return render(request,'accounts/register.html',context={})


def logout_view(request):
    if request.method == "POST":
       logout(request)
       return redirect('/accounts/login')
    return render(request,'accounts/logout.html',context={})