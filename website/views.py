from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    # return HttpResponse('index_view')
    # return HttpResponse('<h1>Home Page<h1>')
    return render(request, 'website/index.html')

def about_view(request):
    # return HttpResponse('<h1>About Page<h1>')
    return render(request, 'website/about.html')

def contact_view(request):
    # return HttpResponse('<h1>Contact Page<h1>')
    return render(request, 'website/contact.html')

def json_test(request):
    return JsonResponse({'name':'ali'})
