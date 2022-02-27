from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def setcookie(request):
    response = render(request, "cookie.html")
    # response.set_cookie(key='name', value="ABC")
    # response.set_cookie(key='age', value='29')
    if request.COOKIES.get('visits'):
        response.set_cookie('data', 'Welcome back')
        value = int(request.COOKIES.get('visits'))
        response.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        response.set_cookie('visits', value)
        response.set_cookie('data', text)
    return response

def homepage(request):
    # print(request.COOKIES.items())
    return HttpResponse("Hola...")

def getcookie(request):
    nm = request.COOKIES.get('name')
    ag = request.COOKIES.get('age')
    print(nm, ag)
    return render(request, "show_cookies.html")

def delete_cookies(request):
    response = redirect('homepage')
    response.delete_cookie('name')
    response.delete_cookie('age')
    return response

def show_cookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('data')
        response = render(request, "show_cookies.html")
        response.set_cookie('visits', int(value) + 1)
        return response
    else:
        return redirect('set_cookie')

# # Session

def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Welcome to Django Session</h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Cookie deleted")
    else:
        response = HttpResponse("Your browser does not accept cookies")
    return response

def demo_view(request):
    print(request.session.__dict__)
    print(request.session.test_cookie_worked())
    return HttpResponse("In demo view")

def create_session(request):
    print(request.session.__dict__)
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    request.session['age'] = 27
    request.session['city'] = 'Pune'
    print(request.session.__dict__)
    return HttpResponse("<h1>The session is set</h1>")

def show_session_data(request):
    print(request.session.items())
    return render(request, "session.html")

def delete_session_data(request):
    print(request.session.items())
    del request.session['name']
    del request.session['password']
    del request.session['age']
    return HttpResponse(f"<h1>Session data deleted: {['name', 'password', 'age']} </h1>")


