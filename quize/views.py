from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from quize.models import quize  ,quize_category,user_start_quize,question,user_answer,answer


def test(request):
    return render(request,'test/main.html')

def quizes(request):
    if 'id' in request.GET:
        cat_id = request.GET['id']
        cat = quize_category.objects.get(id=cat_id)
        quize_data = quize.objects.filter(quize_category=cat.id)
    elif 'search' in request.GET:
        quize_name = request.GET['search']
        quize_data = quize.objects.filter(quize_name__contains=quize_name)
    else:
        quize_data = quize.objects.all()
    context = {
        'quize_data': quize_data,
    }
    return render(request,"quize.html",context)

def start_quize(request,quize_id):
    if 'user_email' in request.session:
        user_email = request.session['user_email']
        if user_start_quize.objects.filter(quize_id=quize_id, user_email=user_email, status="completed").exists():
            messages.error(request, "You Have Already Participated ! You Can Check Result In Profile")
            return redirect('quize')
        else:
            if user_start_quize.objects.filter(quize_id=quize_id, user_email=user_email,status="incompleted").exists():
                pass
            else:
                save_data = user_start_quize(quize_id=quize_id, user_email=user_email, status="incompleted")
                save_data.save()
            question_data = question.objects.filter(quize_id=quize_id)
            quize_data = quize.objects.get(id=quize_id)
            data = Paginator(question_data, 1)
            page = request.GET.get('page')
            try:
                data = data.page(page)
            except:
                data = data.page(1)
            data1 = {}
            i = 1
            for ld in question_data:
                data1[i] = i
                i = i + 1
            xp={}
            l=0
            for x in question_data:
                data1[i] = i
            answer_data = answer.objects.filter(question_id=data.object_list)
            user_answers=user_answer.objects.filter(user_email=request.session['user_email'])
            context={
                'question_data': data.object_list,
                'quize_data': quize_data,
                'answer_data':answer_data,
                'p':data,
                'paginate':data1,
                'user_answer':user_answers,
            }
            return render(request, "start-quize.html",context)
    else:
        messages.error(request, "Login First")
        return redirect('login')



def save_ans(request):
    question_id=request.GET['question_id']
    answer_id = request.GET['answer_id']
    quize_id = request.GET['quize_id']
    user_email=request.session['user_email']
    if user_answer.objects.filter(question_id=question_id,user_email=user_email,quize_id=quize_id).exists():
            data1=user_answer.objects.get(question_id=question_id,user_email=user_email,quize_id=quize_id)
            data1.answer_id=answer_id
            data1.save()
            msg="Answer Updated Successfully"
            return JsonResponse({'status': 0, 'msg': msg})
    else:
        data = user_answer(question_id=question_id, answer_id=answer_id, user_email=user_email,quize_id=quize_id)
        data.save()
        msg = "Answer Saved Succssfully"
        return JsonResponse({'status': 1, 'msg': msg})



def submit_quize(request):
    quize_id=request.GET['quize_id']
    user_email=request.session['user_email']
    save_data = user_start_quize.objects.get(quize_id=quize_id, user_email=user_email)
    save_data.status="completed"
    save_data.save()
    messages.success(request,'Quize Submited Successfully')
    return redirect('quize-result',quize_id=quize_id)


def quize_result(request,quize_id):
        user_email=request.session['user_email']
        quize_data=quize.objects.get(id=quize_id)
        user_answer_data=user_answer.objects.filter(quize_id=quize_id,user_email=user_email)
        ques=question.objects.filter(quize_id=quize_id)
        ans=answer.objects.all()
        correct=0
        mark_for_one_ques=100/(ques.count())
        mark=0
        print(mark_for_one_ques)
        m={}
        i=0
        for user_answers in user_answer_data:
            for answers in answer.objects.filter(question_id=user_answers.question_id):
                if answers.correct_answer==True:
                    if answers.id == int(user_answers.answer_id):
                        print('correct')
                        correct=correct+1
                        mark=mark+mark_for_one_ques
                    else:
                        print('inccorect')
        print(correct,'out of',ques.count())
        context={
            'correct':correct,
            'question':ques,
            'answer':ans,
            'user_answer':user_answer_data,
        }
        return render(request,'quize_result.html',context)

def my_quize(request):
    if 'user_email' in request.session:
        user_email=request.session['user_email']
        quize_data = quize.objects.all()
        user_quize=user_start_quize.objects.filter(user_email=user_email)
        context={
            'quize_data':quize_data,
            'user_quize':user_quize,
        }
        return render(request,"my-quize.html",context)
    else:
        messages.error(request,'Please Login')
        return redirect('login')