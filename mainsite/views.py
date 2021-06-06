from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Post

from django.template.loader import get_template
from datetime import datetime



# 簡單呈現資料庫內容
# def homepage(request):
#     posts = Post.objects.all()
#     post_lists = list()
#     for count, post in enumerate(posts):
#         post_lists.append("No.{}:".format(str(count)) +str(post)+"<br>")
#         post_lists.append(str(post.pub_date)+"<br>")
#         post_lists.append("<small>"+str(post.body)+"</small><br><br>")
#     return HttpResponse(post_lists)

# 使用網頁美化資料呈現
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

# 增加分頁
def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
