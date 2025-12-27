from django.urls import path
from blog.views import *

app_name='blog'  #url

urlpatterns = [
    # path('home',index_view),
    path('', blog_view, name='index'),
    path('single', blog_single, name='single')
]