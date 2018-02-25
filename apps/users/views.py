from django.shortcuts import render
from django.contrib.auth import authenticate, login


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
    # 获取登陆页面为get
    elif request.method == 'GET':
        # 如果用户是用GET方法，则继续要求用户到登陆页面去
        # render就是渲染html返回给用户
        # render 的三个变量：request 模板名称 一个字典写明传给前端的值
        return render(request, 'login.html', {})
