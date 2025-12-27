from django.shortcuts import render

# Create your views here.

def blog_view(request):
    # return HttpResponse('index_view')
    # return HttpResponse('<h1>Home Page<h1>')
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    # return HttpResponse('index_view')
    # return HttpResponse('<h1>Home Page<h1>')
    context={'title':'آموزش زبان انگلیسی مقدماتی سطح A1',
             'content':'این دوره برای افرادی طراحی شده که می‌خواهند زبان انگلیسی را از پایه و بدون هیچ پیش‌زمینه‌ای شروع کنند. محتوای دوره به‌صورت کاربردی و مرحله‌به‌مرحله تنظیم شده تا زبان‌آموز بتواند به‌آسانی مفاهیم پایه را یاد',
             'author':'علی وحدتی'}
    return render(request, 'blog/blog-single.html',context)
