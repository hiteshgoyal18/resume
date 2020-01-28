from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("Hello!! Home Page")
    return render(request, 'hit/login.html')

