from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #THERE IS THIRD ARGUMNET THAT RETURN RENDER TAKES (REQUEST,"HTML FILE NAME",PARAMS)

    return render(request,'index0.html')

def analyze(request):
    print(request.GET) 
    
    djtext=request.POST.get('text', 'default' )
    
    #if it is on then it will print on if not then it will print off
    removepunc=request.POST.get('rf', 'off' )
    capitalizefunc=request.POST.get('cf', 'off' )
    removenewlinerfunc=request.POST.get('rl', 'off' )
    spaceremover=request.POST.get('sr', 'off' )
    charactercount=request.POST.get('cc', 'off' )
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
        djtext=analyzed_text
    
    #CODE TO CAPITALIZE THE TEXT
    if(capitalizefunc=="on"):
        analyzed_text=""
        for char in djtext:
            analyzed_text=analyzed_text+char.upper()
        params={
        "purpose":"Capitalized All Characters",
        "text":analyzed_text
        } 
        djtext=analyzed_text
    
    #CODE TO REMOVE NEW LINE
    if(removenewlinerfunc=="on"):
        print("p")
        print(djtext)
        
        analyzed_text=""
        letters_str = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
        letters_list = letters_str.split(', ')
        letters_str1 ="A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
        letters_list1 = letters_str1.split(', ')
        punctuations=[ '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~']
        my_list = [i for i in range(1, 101)]
        string_list = [str(num) for num in my_list]
        for char in djtext:
            if char == "\n":
                analyzed_text += " "  # Replace newline with a space
            elif char in letters_list or char == " " or char in punctuations or char in string_list or char in letters_list1:
                analyzed_text += char
        print("a")
        # for char in djtext:
        #     if char!="\n" and char!="\r":
        #         analyzed_text += char
        #     else:
        #         print("no")
        params={
        "purpose":"Remove New Lines From Text",
        "text":analyzed_text
        } 
        djtext=analyzed_text

    #CODE TO REMOVE EXTRA SPACES
    if(spaceremover=="on"):
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
        djtext=analyzed_text
    
    #CODE TO COUNT CHARACTERS FROM TEXT
    if(charactercount=="on"):
        punctuations=['"',"'",'/','_']
        analyzed_text=0
        letters_str = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
        letters_list = letters_str.split(', ')
        letters_str1 ="A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
        letters_list1 = letters_str1.split(', ')
        for char in djtext:
            if char in letters_list or char in letters_list1:
                analyzed_text=analyzed_text+1
        d=str(analyzed_text)
        analyzed_text="UR COUNT IS:- " + d
        params={
        "purpose":"Character Count",
        "text":analyzed_text
            } 
        djtext=analyzed_text
    
    if(removepunc=="off" and capitalizefunc=="off" and removenewlinerfunc=="off" and spaceremover=="off" and charactercount=="off"):
        return render(request,'error.html')
    #JO BH OPERATION HOGA USSE 'analyze.html' MAE LEKE JAYEGA
    return render(request,'analyze.html',params)    
                 

