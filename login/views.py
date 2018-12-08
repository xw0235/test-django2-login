from django.shortcuts import render, redirect
from . import models, forms
from .models import User

# Create your views here.


def index(request):

    return render(request, 'login/index.html', locals())


def login(request):
    if request.session.get('is_login', None):
        '''不允许重复登录'''
        return redirect("/index/")
    if request.method == "POST":    # request.method中封装了数据请求的方法，如果是“POST”（全大写），将执行if语句的内容，如果不是，直接返回最后的render()结果
        login_form = forms.UserForm(request.POST)   # request.POST封装了所有POST请求中的数据，这是一个字典类型，可以通过get方法获取具体的值。
        message = "请检查填写的内容！"
        if login_form.is_valid():   # 如果输入框不为空
            u = login_form.cleaned_data['username']
            p = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(username=u)
                if user.password == p:
                    request.session["is_login"] = True
                    request.session["user_id"] = user.id
                    request.session["user_name"] = user.username
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except User.DoesNotExist:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"

        if register_form.is_valid():
            u = register_form.cleaned_data['username']
            p1 = register_form.cleaned_data['password1']
            p2 = register_form.cleaned_data['password2']

            if p1 != p2:
                message = '两次密码输入错误'
                return render(request, 'login/register.html', locals())
            else:
                same = models.User.objects.filter(username=u)
                if same:
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                else:
                    new_user = models.User()
                    new_user.username = u
                    new_user.password = p1
                    new_user.save()
                    return redirect("/login/")

    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect('/index/')

