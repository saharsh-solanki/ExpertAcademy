from django.contrib import messages
from django.shortcuts import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from course.models import course,course_requirements,course_category,access_to,lesson,enrollment,course_comment,course_comment_reply,lesson_comment,lesson_comment_reply


def courses(request):
    if 'id' in request.GET:
        cat_id=request.GET['id']
        cat=course_category.objects.get(id=cat_id)
        course_data = course.objects.filter(course_category=cat.id)
    elif 'search' in request.GET:
        course_name = request.GET['search']
        course_data = course.objects.filter(course_name__contains=course_name)
    else:
        course_data = course.objects.all()
    context={
        'course_data':course_data,
    }
    return render(request,"course.html",context)

def course_detail(request,course_slug):
    course_data = course.objects.get(course_slug=course_slug)
    course_req=course_requirements.objects.filter(course_name=course_data.id)
    access = access_to.objects.filter(course_name=course_data.id)
    lessons = lesson.objects.filter(course_name=course_data.id)
    comment=course_comment.objects.filter(course_id=course_data.id)
    comment_reply = course_comment_reply.objects.all()
    recent_course=course.objects.filter().order_by('-id')[:4]
    category = course_category.objects.filter().order_by('?')[:5]
    context = {
        'course_data': course_data,
        'course_requirements':course_req,
        'access_to':access,
        'lesson':lessons,
        'comment':comment,
        'comment_reply':comment_reply,
        'recent_course':recent_course,
        'category':category,
    }
    return render(request,"course-detail.html",context)

def learn_course(request,course_slug):
    if 'user_email' in request.session:
        user_email=request.session['user_email']
        courses = course.objects.get(course_slug=course_slug)
        if enrollment.objects.filter(user_email=user_email,course_id=courses.id).exists():
            lesson_data=lesson.objects.filter(course_name=courses.id)
            page = request.GET.get('page', 1)
            paginator = Paginator(lesson_data, 1)
            try:
                ls = paginator.page(page)
            except PageNotAnInteger:
                ls = paginator.page(1)
            except EmptyPage:
                ls = paginator.page(paginator.num_pages)
            data1={}
            i=1
            for ld in lesson_data:
                data1[ld.id]=i
                i=i+1
            lesson_comments =lesson_comment.objects.filter(lesson_id=ls.object_list)
            lesson_comments_reply = lesson_comment_reply.objects.all()
            context = {
                'lesson_data' :lesson_data,
                'current_lesson':ls.object_list,
                'ls':ls,
                'up_lesson':data1,
                'comment':lesson_comments,
                'comment_reply':lesson_comments_reply,
                'course_slug':course_slug,
            }
            return render(request, "learn-course.html", context)
        else:
            messages.error(request,'You Have  Not Enrolled For This Course Yet')
            return redirect('learn-course',course_name=courses.course_slug)
    else:
        messages.success(request,'Please Login To Enroll !')
        return redirect('login')


def enroll_course(request,course_name):
    if 'user_email' in request.session:
        courses = course.objects.get(id=course_name)
        user_email=request.session['user_email']
        if enrollment.objects.filter(course_id=course_name,user_email=user_email).exists():
            messages.success(request,'You Have Already Enrolled For This Course!')
            return redirect('learn-course',course_slug=courses.course_slug)
        else:
            enroll = enrollment(course_id=course_name,user_email=user_email)
            enroll.save()
            messages.success(request,'Enrolled Successfully Start Learning!')
            return redirect('learn-course',course_slug=courses.course_slug)
    else:
        messages.success(request,'Please Login To Enroll !')
        return redirect('login')


def do_course_comment(request):
    course_id=request.POST['course_id']
    course_slug = request.POST['course_slug']
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    data=course_comment(course_id=course_id,user_name=name,user_email=email,comment=message)
    data.save()
    return redirect('course-detail',course_slug=course_slug)


def do_course_comment_reply(request):
    comment_id=request.POST['comment_id']
    course_slug = request.POST['course_slug']
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    data=course_comment_reply(comment_id=comment_id,user_name=name,user_email=email,comment=message)
    data.save()
    messages.success(request,'Comment Success')
    return redirect('course-detail',course_slug=course_slug)

def do_lesson_comment(request):
    page=request.POST['page']
    lesson_id=request.POST['lesson_id']
    course_slug = request.POST['course_slug']
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    data = lesson_comment(lesson_id=lesson_id, user_name=name, user_email=email, comment=message)
    data.save()
    messages.success(request, 'Comment Success')
    return redirect('learn-course/'+course_slug+'?page='+page)




def do_lesson_comment_reply(request):
    page = request.POST['page']
    lesson_comment_id = request.POST['lesson_comment_id']
    course_slug = request.POST['course_slug']
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    data=lesson_comment_reply(lesson_comment_id=lesson_comment_id,user_name=name,user_email=email,comment=message)
    data.save()
    messages.success(request, 'Comment Success')
    return redirect('learn-course/' + course_slug + '?page=' + page)


def my_course(request):
    if 'user_email' in request.session:
        user_email = request.session['user_email']
        course_data = course.objects.all()
        user_course = enrollment.objects.filter(user_email=user_email)
        context={
            'course_data':course_data,
            'user_course':user_course,
        }
        return render(request,"my-course.html",context)
    else:
        messages.error(request, 'Login To Access Profile')
        return redirect('login')


def mark_as_completed(request):
    if 'user_email' in request.session:
        user_email=request.session['user_email']
        lesson_id=request.GET['lesson_id']
        lesson_data=lesson.objects.get(id=lesson_id)
        courses=course.objects.get(course_name=lesson_data.course_name)
        data=enrollment.objects.get(user_email=user_email,course_id=courses.id)
        data.status='completed'
        data.save()
        messages.success(request, 'Marked This Course As Completed')
        return redirect('learn-course' , course_slug=courses.course_slug)
    else:
        messages.success(request,'login First')
        return redirect('login')