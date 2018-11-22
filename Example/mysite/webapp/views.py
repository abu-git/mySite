from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2>Hello World</h2>" + '<a href="about">Click me!</a>')

def about(request):
	return render(request, 'webapp/about.html')
