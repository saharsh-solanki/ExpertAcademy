from django.shortcuts import render

# Create your views here.
import random
from datetime import datetime
import random
import string

from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import get_template
from user.models import user_data
from ExpertAcademy import settings


def register(request):
    if request.method=="POST":
        name=request.POST['name']
        age = request.POST['age']
        email=request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        gender = request.POST['gender']
        if email=="":
            msg="Enter Your Email"
            return JsonResponse({'status': 1, 'msg': msg})
        elif password=="":
            msg="Enter Your Password"
            return JsonResponse({'status': 1, 'msg': msg})
        elif phone=="":
            msg="Enter Your Phone Number"
            return JsonResponse({'status': 1, 'msg': msg})
        elif user_data.objects.filter(email=email).exists():
            msg="Your Account IS Already Available Please Login !"
            return JsonResponse({'status': 1, 'msg': msg})
        elif user_data.objects.filter(phone=phone).exists():
            msg="This Mobile Is Used By Another Account"
            return JsonResponse({'status': 1, 'msg': msg})
        elif name=="":
            msg="Enter Your Name"
            return JsonResponse({'status': 1, 'msg': msg})
        elif age=="":
            msg="Enter Your Age"
            return JsonResponse({'status': 1, 'msg': msg})
        else:
            otp=random.randint(1000,9999)
            subject = "ONE TIME PASSWORD VERIFCTAION CODE"
            sender = settings.EMAIL_HOST_USER
            to = email
            title="OTP FOR EMAIL VERIFCATION "
            message="One Time Password For Your Account Regitration"
            ctx = {
                'title':title,
                'otp':otp,
                'content': message,
            }
            message = get_template('forms/email.html').render(ctx)
            msg = EmailMessage(
                subject,
                message,
                sender,
                [to],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
            request.session['otp_from_server']=otp
            request.session['name'] = name
            request.session['email'] = email
            request.session['password'] = password
            request.session['age'] = age
            request.session['gender'] = gender
            request.session['phone'] = phone
            msag="OTP Sended To Your Email Check Spam Folder Also !!"
            return JsonResponse({'status': 0})
    else:
        return render(request,"forms/registration_form.html")

#function for Otp Varification
def verify_otp(request):
    if request.method == "POST":
        name = request.session['name']
        email = request.session['email']
        password = request.session['password']
        age = request.session['age']
        phone = request.session['phone']
        gender = request.session['gender']
        otp_by_user=str(request.POST['otp_from_user'])
        otp_by_server=str(request.session['otp_from_server'])
        if otp_by_user!=otp_by_server:
            msg="incorrect Otp"
            return JsonResponse({'status': 1, 'msg': msg})
        else:
            user=user_data(name=name,email=email,password=password,age=age,phone=phone,gender=gender)
            user.save()
            cont="Congratulation You Have Successfully registered"
            send_mail(
                "Registration Successfull",
                cont,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            msg="Registered Successfully !! Redirecting To Login......."
            request.session.flush()
            return JsonResponse({'status':0,'msg':msg})
    else:
        return render(request,'forms/varify-otp.html')

def resend_reg_otp(request):
   otp = random.randint(1000, 9999)
   subject = settings.site_name+" OTP For Email Verifcation"
   sender = settings.EMAIL_HOST_USER
   to = request.session['email']
   title = "Email Varification"
   message = "One Time Password For Your Account Regitration"
   ctx = {
                'title': title,
                'otp': otp,
                'content': message,
            }
   message = get_template('forms/email.html').render(ctx)
   msg = EmailMessage(
   subject,
   message,
   sender,
   [to],
            )
   msg.content_subtype = "html"  # Main content is now text/html
   msg.send()
   request.session['otp_from_server'] = otp
   msg='OTP Resended To Your Email Check Spam Folder '
   return JsonResponse({'status':0,'msg':msg})


def reset_password(request):
    if request.method=="POST":
        email=request.POST['email']
        if user_data.objects.filter(email=email).exists():
            otp = random.randint(1000, 9999)
            subject = settings.EMAIL_HOST_USER
            sender = settings.site_name+"  OTP Verification"
            to = email
            title = "Email Varification"
            message = "Use The Below Code To Register Your Account "
            ctx = {
                'title': title,
                'otp': otp,
                'content': message,
            }
            message = get_template('forms/email.html').render(ctx)
            msg = EmailMessage(
                subject,
                message,
                sender,
                [to],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
            request.session['otp_from_server'] = otp
            request.session['email'] = email
            msg="Verification Code Sended To Your Email Check Spam Folder If Not Recived"
            return JsonResponse({'status':0,'msg':msg})
        else:
            #now We Need To Genrate 4 Digit Random Number And Send It To Mail
            msg = "The Email You Have Provided Is Not Registred With Us !! If Your New To Here You Need To Create Your Account First "
            return JsonResponse({'status':1,'msg':msg})
    else:
        return render(request,"forms/reset_password_form.html")

def varify_reset_password_otp(request):
    if request.method == "POST":
        email = request.session['email']
        password = request.POST['password']
        otp_by_user= str(request.POST['otp'])
        otp_by_server = str(request.session['otp_from_server'])
        if otp_by_user != otp_by_server:
            msg="incorrect Otp"
            return JsonResponse({'status':1,'msg':msg })
        else:
            user=user_data.objects.get(email=email)
            user.password=password
            user.save()
            request.session.flush()
            msg="Password Updated Successfully !! Redirecting You To Login"
            return JsonResponse({'status':0,'msg':msg })
    else:
        return render(request,'forms/reset_password_varify_otp.html')

def resend_reset_password_otp(request):
    otp = random.randint(1000, 9999)
    # code To Send Otp To Email
    subject = "OTP For Email Verifcation"
    sender = settings.EMAIL_HOST_USER
    to = request.session['email']
    title = "Email Varification"
    message = "One Time Password For Your Account Regitration"
    ctx = {
        'title': title,
        'otp': otp,
        'content': message,
    }
    message = get_template('forms/email.html').render(ctx)
    msg = EmailMessage(
        subject,
        message,
        sender,
        [to],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    request.session['otp_from_server'] = otp
    msgs="A New OTP Is Sended To Email Check Your Mail Check Spam Folder Also"
    return JsonResponse({'status':0,'msg':msgs })



# login function
def login(request):
    if 'user_email' in request.session:
        return redirect('course')
    else:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            if email == "":
                msg = "Enter Your Email"
                return JsonResponse({'status': 1, 'msg': msg})
            elif password == "":
                msg = "Enter Your Password"
                return JsonResponse({'status': 1, 'msg': msg})
            elif user_data.objects.filter(email=email).exists():
                if user_data.objects.filter(email=email, password=password).exists():
                    msg = "Login-In Successfuly!! Redirecting To Dashboard ....... "
                    user = user_data.objects.get(email=email)
                    request.session['user_email'] = email
                    request.session['user_name'] = user.name
                    return JsonResponse({'status': 0, 'msg': msg})
                else:
                    msg = "Inccorect Password !"
                    return JsonResponse({'status': 1, 'msg': msg})
            else:
                msg = "This Email Address Is Not Registered With Us!"
                return JsonResponse({'status': 1, 'msg': msg})
        else:
          return render(request, "forms/login.html")



#function logoutuser data
def logout(request):
    #del request.session['user_name']
    #del request.session['user_email']
    request.session.flush()
    msg="logout Successfully"
    return render(request,'index.html',{'msg':msg})