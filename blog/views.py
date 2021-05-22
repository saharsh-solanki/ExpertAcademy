from django.contrib import messages
from django.shortcuts import render, redirect
from blog.models import blog_category,blog,blog_comment_reply,blog_comment
# Create your views here.
def blogs(request):
    if 'id' in request.GET:
        cat_id = request.GET['id']
        cat = blog_category.objects.get(id=cat_id)
        blog_data = blog.objects.filter(blog_category=cat.id)
    elif 'search' in request.GET:
        blog_name = request.GET['search']
        blog_data = blog.objects.filter(blog_tittle__contains=blog_name)
    else:
        blog_data = blog.objects.all()

    recent_blog = blog.objects.filter().order_by('-id')[:4]
    category = blog_category.objects.filter().order_by('?')[:5]
    comment_data=blog_comment.objects.all()
    context = {
        'recent_blog':recent_blog,
         'category': category,
        'blog_data': blog_data,
        'comment_data':comment_data,
    }
    return render(request,"blog.html",context)

def blog_post(request,blog_name):
    if 'x' in request.GET:
        blog_data = blog.objects.get(blog_slug=blog_name)
        comment = blog_comment.objects.filter(blog_id=blog_data.id)
        comment_reply = blog_comment_reply.objects.all()
        recent_blog = blog.objects.filter().order_by('-id')[:4]
        category = blog_category.objects.filter().order_by('?')[:5]
        context = {
            'blog_data': blog_data,
            'comment': comment,
            'comment_reply': comment_reply,
            'recent_blog': recent_blog,
            'category': category,
        }
        return render(request, "blog-post.html", context)
    else:
        try:
            blog_data = blog.objects.get(blog_slug=blog_name)
            print(blog_data.date)
            comment = blog_comment.objects.filter(blog_id=blog_data.id)
            comment_reply = blog_comment_reply.objects.all()
            recent_blog = blog.objects.filter().order_by('-id')[:4]
            category = blog_category.objects.filter().order_by('?')[:5]
            context = {
                'blog_data': blog_data,
                'comment': comment,
                'comment_reply': comment_reply,
                'recent_blog': recent_blog,
                'category': category,
            }
            return render(request, "blog-post.html", context)
        except:
            return redirect('blog')


def do_blog_comment(request):
    blog_id=request.POST['blog_id']
    blog_slug = blog.objects.get(id=blog_id)
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    data = blog_comment(blog_id=blog_id, user_name=name, user_email=email, comment=message)
    data.save()
    messages.success(request,'Commented Succeess Wait For Reply')
    return redirect('blog-post/'+blog_slug.blog_slug+'?x=1')




def do_blog_comment_reply(request):
    blog_comment_id = request.POST['blog_comment_id']
    blog_slug = blog.objects.get(id=blog_comment.objects.get(id=blog_comment_id).blog_id)
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    data=blog_comment_reply(blog_comment_id=blog_comment_id,user_name=name,user_email=email,comment=message)
    data.save()
    messages.success(request, 'Reply Success')
    return redirect('blog-post/'+blog_slug.blog_slug+'?x=1')

