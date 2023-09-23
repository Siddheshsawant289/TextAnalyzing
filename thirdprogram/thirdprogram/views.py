from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #THERE IS THIRD ARGUMNET THAT RETURN RENDER TAKES (REQUEST,"HTML FILE NAME",PARAMS)
    params={
        "NAME":"siddhesh",
        "PROJECT_DEVELOPED":"django developer"
        }
    return render(request,'index.html',params)

def removepunc(request):
    return render(request,'index1.html')
                 

def capitalizefirst(request):

    return render(request,'index2.html')

def newlineremove(request):

    return render(request,'index3.html')

def spaceremove(request):

    return render(request,'index4.html')

def charactercount(request):

    return render(request,'index5.html')