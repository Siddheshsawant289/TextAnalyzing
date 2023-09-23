from django.http import HttpResponse

def index(request):
    html_content='''
<html>
    <head>
        <title>Button with Anchor Tag</title>
    </head>
    <body style="background-color: #f0f0f0; text-align: center; font-family: Arial, sans-serif;">
        <h1 style="color: #0070e0; margin-top: 100px;">Welcome to my app</h1>
        <button>
            <a href="http://127.0.0.1:8000/removepunc">Next</a>
        </button>
    </body>
    </html>

'''
    return HttpResponse(html_content)

def removepunc(request):
    html_content='''
<html>
    <head>
        <title>Button with Anchor Tag</title>
    </head>
    <body style="background-color: #f0f0f0; text-align: center; font-family: Arial, sans-serif;">
        <h1 style="color: #0070e0; margin-top: 100px;">Welcome to my Removefunc</h1>
        <button>
            <a href="http://127.0.0.1:8000/capitalizefirst">Next</a>
        </button>
        <br></br>
        <button>
            <a href="http://127.0.0.1:8000/">Back</a>
        </button>        
    </body>
    </html>

'''
    return HttpResponse(html_content)
    

def capitalizefirst(request):
    html_content='''
<html>
    <head>
        <title>Button with Anchor Tag</title>
    </head>
    <body style="background-color: #f0f0f0; text-align: center; font-family: Arial, sans-serif;">
        <h1 style="color: #0070e0; margin-top: 100px;">Welcome to my Capitalizefirst </h1>
        <button>
            <a href="http://127.0.0.1:8000/newlineremove">Next</a>
        </button>
        <br></br>
        <button>
            <a href="http://127.0.0.1:8000/removepunc">Back</a>
        </button>        
    </body>
    </html>

'''
    return HttpResponse(html_content)

def newlineremove(request):
    html_content='''
<html>
    <head>
        <title>Button with Anchor Tag</title>
    </head>
    <body style="background-color: #f0f0f0; text-align: center; font-family: Arial, sans-serif;">
        <h1 style="color: #0070e0; margin-top: 100px;">Welcome to my Newlineremove </h1>
        <button>
            <a href="http://127.0.0.1:8000/spaceremove">Next</a>
        </button>
        <br></br>
        <button>
            <a href="http://127.0.0.1:8000/capitalizefirst">Back</a>
        </button>        
    </body>
    </html>

'''
    return HttpResponse(html_content)

def spaceremove(request):
    html_content='''
<html>
    <head>
        <title>Button with Anchor Tag</title>
    </head>
    <body style="background-color: #f0f0f0; text-align: center; font-family: Arial, sans-serif;">
        <h1 style="color: #0070e0; margin-top: 100px;">Welcome to my Spaceremove </h1>
        <button>
            <a href="http://127.0.0.1:8000/charactercount">Next</a>
        </button>
        <br></br>
        <button>
            <a href="http://127.0.0.1:8000/newlineremove">Back</a>
        </button>        
    </body>
    </html>

'''
    return HttpResponse(html_content)

def charactercount(request):
    html_content='''
<html>
    <head>
        <title>Button with Anchor Tag</title>
    </head>
    <body style="background-color: #f0f0f0; text-align: center; font-family: Arial, sans-serif;">
        <h1 style="color: #0070e0; margin-top: 100px;">Welcome to my Charactercount </h1>
        <button>
            <a href="http://127.0.0.1:8000/spaceremove">Back</a>
        </button>        
    </body>
    </html>

'''
    return HttpResponse(html_content)