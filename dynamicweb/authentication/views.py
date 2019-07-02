from django.shortcuts import render, redirect
import hashlib

from .models import userdata
from authentication.forms import LoginForm,SignupForm
from application.models import Menu

# A VIEW TO DISPLAY THE FORM REQUIRED TO LOGIN
def form_to_login(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return redirect(login)
    else:
        return render(request, 'login.html', {'text':''})

# A VIEW TO CHECK LOGIN CREDENTIALS OF THE USER
# IF SESSION IS EXISTING, THEN IT WILL SHOW HOME PAGE

def login(request):
    if request.session.has_key('username'):
        username = request.session['username']
        navbarcode=""
        dbusername=Menu.objects.filter(username=username)
        if dbusername:
            list=Menu.objects.all()
            for elements in list:
                if elements.username==username:
                    navbarcode=elements.navbarcode
        return render(request, 'loggedin.html', {"username" : username,'navbarcode':navbarcode})
    else:
        username=""
        if request.method == "POST":
            MyLoginForm = LoginForm(request.POST)
            if MyLoginForm.is_valid():
                username = MyLoginForm.cleaned_data['username']
                password=MyLoginForm.cleaned_data['password']
                password=hashlib.md5(password.encode())
                password=password.hexdigest()
                dbusername = userdata.objects.filter(username = username)
                dbpassword = userdata.objects.filter(password = password)
                if not dbpassword:
                    if not dbusername:
                        return render(request, 'login.html', {'text':'ENTER CORRECT DETAILS'})
                    else:
                        return render(request, 'login.html', {'text':'ENTER CORRECT PASSWORD'})
                if not dbusername:
                    return render(request, 'login.html', {'text':'ENTER CORRECT DETAILS'})
                request.session['username'] = username
            else:
                MyLoginForm = LoginForm()
    if not username:
        return redirect(form_to_login)
    navbarcode=""
    dbusername=Menu.objects.filter(username=username)
    if dbusername:
        list=Menu.objects.all()
        for elements in list:
            if elements.username==username:
                navbarcode=elements.navbarcode
    return render(request,'loggedin.html',{'username':username,'navbarcode':navbarcode})
   
# A VIEW TO LOGOUT THE USER

def logout(request):
    try:
       del request.session['username']
    except:
       pass
    return redirect('/')

# A VIEW TO DISPLAY THE SIGNUP PAGE
# IT WILL THEN REDIRECT TO HOME PAGE

def signup(request):
    if request.method=='POST':
        email_f=request.POST.get('email')
        username_f=request.POST.get('username')
        password_f=request.POST.get('password')
        password_f=hashlib.md5(password_f.encode())
        password_f=password_f.hexdigest()
        dbusername = userdata.objects.filter(username = username_f)
        dbemail=userdata.objects.filter(email = email_f)
        if dbemail :
            text="this email is existing."
            return render(request,'signup.html',{'text':text})
        if dbusername:
            text="this username is existing."
            return render(request,'signup.html',{'text':text})
        new_obj=userdata(email=email_f,username=username_f,password=password_f)
        new_obj.save()
        request.session['username'] = username_f
        return redirect(login)
    else:
        return render(request,'signup.html',{})