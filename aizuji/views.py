from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def menu(request) :
    context = {}
    context['hello'] = '爱租机自动化测试管理平台'
    context['cases'] = "<a href='http://127.0.0.1:8000/cases'>测试用例</a>"
    context['task'] = "<a href='http://127.0.0.1:8000/task'>测试任务</a>"
    context['environment'] = "<a href='http://127.0.0.1:8000/environment'>测试环境</a>"
    context['interface'] = "<a href='http://127.0.0.1:8000/interface'>接口管理</a>"
    context['login'] = "<a href='http://127.0.0.1:8000/login'>登陆</a>"
    return render(request,"menu.html",context )

def cases(request) :
    context = {}
    context['ccc'] = '测试用例界面'
    return render(request,"cases.html",context )


def environment(request) :
    context = {}
    context['aaa'] = '测试环境界面'
    return render(request,"cases.html",context )


def task(request) :
    context = {}
    context['zzz'] = '测试任务界面'
    return render(request,"cases.html",context )




# def index(request) :
#     context = {}
#     context['login'] = '登陆'
#     return render(request,"login.html",context )

# def login(request) :
#     context = {}
#     context['login'] = '登录'
#     return render(request,"login.html",context )

# def login(request) :
#     context = {}
#     context['kkk'] = '接口管理'
#     return render (request,'login.html',context )


def login(request) :
    if request.method == 'POST':
        print(request.method)
        if request["username"]=='123' and request["pass"]=='123':
            return render(request,"menu.html")
    else:
        pass
    return render (request,'login.html')



