from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    request.session.set_test_cookie()
    return HttpResponse("<h2>Home Page</h2>")


def page2(request):
    if request.session.test_cookie_worked():
        print("Cookies are enabled!")
        request.session.delete_test_cookie()
    return HttpResponse("<h2>Page 2</h2>")
