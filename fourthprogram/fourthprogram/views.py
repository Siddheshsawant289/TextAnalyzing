from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #THERE IS THIRD ARGUMNET THAT RETURN RENDER TAKES (REQUEST,"HTML FILE NAME",PARAMS)
    params={
        "NAME":"siddhesh",
        "PROJECT_DEVELOPED":"django developer"
        }
    return render(request,'index0.html',params)

def removepunc(request):
    #GET THE TEXT
    #THIS WILL SHOW U THE TEXT COMMING FROM ANOTHER HTML
    print(request.GET) 
    
    #HERE TEXT THAT HAS BEEN PASSED FROM ANOTHER HTML IF TEXT IS NOT PRESENT IT WILL SHOW DEFALUT
    #print(request.GET.get('text', 'default' ))
    htmltext=request.GET.get('text', 'default' )

    params={
        "name":htmltext
    }

    return render(request,'index01.html',params)
                 

def capitalizefirst(request):

    return render(request,'index02.html')

def newlineremove(request):

    return render(request,'index03.html')

def spaceremove(request):

    return render(request,'index04.html')

def charactercount(request):

    return render(request,'index05.html')