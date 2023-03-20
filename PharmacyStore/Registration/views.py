from django.http import HttpResponse
from django.shortcuts import redirect, render

from Registration.models import Registration

# Create your views here.
def loginForm(request):
    data={
        'title':'Member Registration'
    }
    return render(request,"Registration/login.html",data)

def signform(request):
    data={
        'title':'signup'
    }
    return render(request,"Registration/signup.html",data)

def registrationStore(request):
    if request.method =='POST':
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password != cpassword:
            return HttpResponse("Your password and confirm password doesnot match!!")
        else:
            registration= Registration(
                email = request.POST['email'],
                full_name=request.POST['full_name'],
                dob=request.POST['dob'],
                password=request.POST['password'],
                cpassword=request.POST['cpassword'],
                created_at=request.POST.get('created_at', False),
                updated_at=request.POST.get('updated_at',False),

            )
            registration.save()
            return redirect('registration.login')
        return render(request,'registration/signup.html')
            

