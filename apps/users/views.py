from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import UserProfile
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# 当我们配置url被这view处理时，自动传入request对象

def user_login(request):
    # 前端向后端发送的请求方式：GET或者POST
    # 登陆提交表单为POST

    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html', )
        else:
            return render(request,'login.html',{'msg':'用户名或者密码错误！'})
    # 获取登陆页面为get
    elif request.method == 'GET':
        # 如果用户是用GET方法，则继续要求用户到登陆页面去
        # render就是渲染html返回给用户
        # render 的三个变量：request 模板名称 一个字典写明传给前端的值
        return render(request, 'login.html', {})
