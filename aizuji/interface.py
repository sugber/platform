from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from TestModel.models import aizuji

# def interface(request):
#     casename = request.POST.get('casename',None)
#     data = request.POST.get('data',None)
#     url = request.POST.get('url',None)
#     method = request.POST.get('method',None)
#     type = request.POST.get('type',None)
asc = []

def interface(request) :
    aaa = []
    list = aizuji.objects.all ()
    for var in list :
        bbb = {}
        bbb["casename"] = var.casename
        bbb["data"] = var.data
        bbb["url"] = var.url
        bbb["method"] = var.method
        bbb["type"] = var.type
        print("bbb",bbb)
        aaa.append(bbb)
        print("aaa",aaa)
    sss = {}
    sss["aaa"] = aaa
    if request.method == 'POST':
        casename = request.POST.get ( 'casename', None )
        url = request.POST.get ( 'url', None )
        data = request.POST.get ( 'data', None )
        method = request.POST.get ( 'method', None )
        type = request.POST.get ( 'type', None )
        test1 = aizuji ( casename=casename, url=url, data=data, method=method, type=type )
        test1.save()
        asz = 123
        return render(request,"interface.html",sss )
    else:
        return render(request,"interface.html",sss)