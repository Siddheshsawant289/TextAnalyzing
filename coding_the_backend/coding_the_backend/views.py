from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #THERE IS THIRD ARGUMNET THAT RETURN RENDER TAKES (REQUEST,"HTML FILE NAME",PARAMS)

    return render(request,'index0.html')

def analyze(request):
    #GET THE TEXT
    #THIS WILL SHOW U THE TEXT COMMING FROM ANOTHER HTML
    print(request.GET) 
    
    #HERE TEXT THAT HAS BEEN PASSED FROM ANOTHER HTML IF TEXT IS NOT PRESENT IT WILL SHOW DEFALUT
    #print(request.GET.get('text', 'default' ))
    djtext=request.GET.get('text', 'default' )
    #if it is on then it will print on if not then it will print off
    removepunc=request.GET.get('rf', 'off' )
    capitalizefunc=request.GET.get('cf', 'off' )
    removenewlinerfunc=request.GET.get('rl', 'off' )
    spaceremover=request.GET.get('sr', 'off' )
    charactercount=request.GET.get('cc', 'off' )
    #print(djtext)
    # print(removepunc)
    # print(capitalizefunc)
    #print(removenewlinerfunc)
    # print(spaceremover)

    #CODE TO REMOVE PUNCUTATIONS
    if removepunc=="on":
        punctuations=[ '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~']
        analyzed_text=""
        for char in djtext:
            if char not in punctuations:
                analyzed_text=analyzed_text+char
            #print(analyzed_text)
        params={
        "purpose":"Remove Punctuations",
        "text":analyzed_text
        }
    #CODE TO CAPITALIZE THE TEXT
    elif(capitalizefunc=="on"):
        analyzed_text=""
        for char in djtext:
            analyzed_text=analyzed_text+char.upper()
        params={
        "purpose":"Capitalized All Characters",
        "text":analyzed_text
        } 
    #CODE TO REMOVE NEW LINE
    elif(removenewlinerfunc=="on"):
        print("p")
        print(djtext)
        
        analyzed_text=""
        letters_str = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
        letters_list = letters_str.split(', ')
        punctuations=[ '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~']
        my_list = [i for i in range(1, 101)]
        string_list = [str(num) for num in my_list]
        for char in djtext:
            if char == "\n":
                analyzed_text += " "  # Replace newline with a space
            elif char in letters_list or char == " " or char in punctuations or char in string_list:
                analyzed_text += char


        print("a")

        params={
        "purpose":"Remove New Lines From Text",
        "text":analyzed_text
        } 

    # elif(spaceremover=="on"):
    #     analyzed_text=""
    #     for char in djtext:
    #         if char !=" ":
    #             analyzed_text=analyzed_text+char
    #     params={
    #     "purpose":"Remove Spaces From Text",
    #     "text":analyzed_text
    #     } 
    elif(spaceremover=="on"):
        analyzed_text=""
        #n  ame  
        #for index=0 char=_ it will     for index=1 char=_ it will go into else loop and will convert two spaces to one spaces
        for index,char  in enumerate(djtext):
            if  djtext[index] == " "  and  djtext[index+1] == " ":
                pass
            else:
                analyzed_text=analyzed_text+char

        params={
        "purpose":"Remove Spaces From Text",
        "text":analyzed_text
            } 
    #CODE TO COUNT CHARACTERS FROM TEXT
    elif(charactercount=="on"):
        punctuations=['"',"'",'/','_']
        analyzed_text=0
        letters_str = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
        letters_list = letters_str.split(', ')

        for char in djtext:
            if char in letters_list:
                analyzed_text=analyzed_text+1
        params={
        "purpose":"Character Count",
        "text":analyzed_text
            } 
    else:
        return HttpResponse("error")


    
    return render(request,'analyze.html',params)    
                 

# def capitalizefirst(request):

#     return render(request,'index02.html')

# def newlineremove(request):

#     return render(request,'index03.html')

# def spaceremove(request):

#     return render(request,'index04.html')

# def charactercount(request):

#     return render(request,'index05.html')