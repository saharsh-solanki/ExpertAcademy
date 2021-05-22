from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import *

from user.models import user_data,certificate,user_query
from course.models import enrollment

from course.models import course


def index(request):
    course_data=course.objects.filter().order_by('?')[:4]
    context={
        'course_data':course_data,
    }
    return render(request,"index.html",context)




def profile(request):
    if 'user_email' in request.session:
        user_email = request.session['user_email']
        user=user_data.objects.get(email=user_email)
        badge=certificate.objects.filter(user_email=user_email)
        context={
            'user':user,
            'badge':badge,
        }
        return render(request,"profile.html",context)
    else:
        messages.success(request,'Login To Access Profile')
        return redirect('login')

def update_profile(request):
    name = request.GET['name']
    age = request.GET['age']
    if 'gender' in request.GET:
        gender=request.GET['gender']
    else:
        gender = 'male'
    user_email=request.session['user_email']
    user=user_data.objects.get(email=user_email)
    user.name=name
    user.age=age
    user.gender=gender
    user.save()
    return JsonResponse({'status':0,'msg':'Your Profile Update Successfully'})


def update_profile_image(request):
    if request.method == "POST":
        photo = request.FILES['photo']
        user_email=request.session['user_email']
        user=user_data.objects.get(email=user_email)
        user.profile_photo=photo
        user.save()
        messages.success(request,'Your Profile Image Updated Successfully')
    else:
        pass
    return redirect('profile')

def change_password(request):
    new_password = request.GET['new_password']
    new_confirm_password = request.GET['new_confirm_password']
    user_email=request.session['user_email']
    if new_password == new_confirm_password:
        user=user_data.objects.get(email=user_email)
        user.password=new_password
        user.save()
        return JsonResponse({'status':0,'msg':'Your Password Updated Successfully'})
    else:
        return JsonResponse({'status': 0, 'msg': 'Password Do Not Match'})


def fun_certificate(request):
    if 'user_email' in request.session:
        user_email = request.session['user_email']
        cert_data = certificate.objects.filter(user_email=user_email)
        context={
            'certificate':cert_data,
        }
        return render(request,'certificate.html',context)
    else:
        messages.success('Login To Show Data')
        redirect('login')


def apply_for_certificate(request):
    if request.method == "POST":
        user_email = request.session['user_email']
        course_name = request.POST['course_name']
        if certificate.objects.filter(user_email=user_email,course_name=course_name).exists():
            messages.success(request,'You Have Already Apply for certificate For This Course')
        else:
            cert = certificate(course_name=course_name, user_email=user_email, status='pending')
            cert.save()
        return redirect('apply-for-certificate')
    else:
        if 'user_email' in request.session:
            user_email = request.session['user_email']
            cert_data = enrollment.objects.filter(user_email=user_email,status='completed')
            courses=course.objects.all()
            context={
                'user_course':cert_data,
                'course':courses,
            }
            return render(request,'apply_certificate.html',context)
        else:
            messages.success('Login To Show Data')
            redirect('login')

def contact_us(request):
    if request.method== "POST":
        name=request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data=user_query(name=name,email=email,subject=subject,message=message)
        data.save()
        context={}
        send_mail(
            'subject',
            message,
            'New Query',
            ['solankiharsh5888@gmail.com'],
            fail_silently=False,
        )
        messages.success(request,'We Have Recived Your Query ! We Will Get Back To You Within 24 Hour')
        return redirect('contact-us')
    else:
        return render(request, "contact.html")


def about_us(request):
    return render(request,"about_us.html")

