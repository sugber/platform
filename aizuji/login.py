from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def login(request):
    if request.method == 'POST':
        message = {}
        user = request.POST.get('username', None)
        pwd = request.POST.get('password',None)
        if user == '123' and pwd == '123':
            return redirect('/woaizuji')
        else:
            message["message"] = '帐号或密码错误,请重新输入'
            return render(request,"login.html",message)
    else:
        return render(request,"login.html")
        # return redirect("https://www.baidu.com/")