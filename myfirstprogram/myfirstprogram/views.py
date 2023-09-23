#WE SHOULD MAKE VIEWS.PY FILE BY OWN HERE WE WRITE ALL OUR PYTHON CODE
#request should be written or if not written we will get type error

#Because view return response
from django.http import HttpResponse

def index(request): 
    return HttpResponse("Hello"+"<h1>Hello</h1>")
    #return HttpResponse("<h1>Hello</h1>")

def about(request): 
    return HttpResponse("<h1>Hello Guys</h1>")
    #return HttpResponse("<h1>Hello</h1>")

#Always write one return in on function or if written another return it will say unreachable prompt
# When you're returning an HTTP response with HTML content in Django,
#  you should pass the HTML content as a string,
#  not directly as HTML tags within the HttpResponse function call.
def home(request):
    html_content = """
    <html>
    <head>
        <title>Welcome to Django</title>
    </head>
    <body style="background-color: #f0f0f0; text-align: center; font-family: Arial, sans-serif;">

        <h1 style="color: #0070e0; margin-top: 100px;">Welcome to Django</h1>

        <p style="font-size: 18px; color: #333;">This is a simple HTML page with inline CSS.</p>

    </body>
    </html>
    """
    return HttpResponse(html_content)


def nav(request):
    htmlcontent="""
    <html>
    <head>
        <title>Button with Anchor Tag</title>
    </head>
    <body style="background-color: #f0f0f0; text-align: center; font-family: Arial, sans-serif;">
        <h1 style="color: #0070e0; margin-top: 100px;">Welcome to Personal Navigator</h1>
        <button>
            <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Visit This Website</a>
        </button>
    </body>
    </html>
    """
    return HttpResponse(htmlcontent)