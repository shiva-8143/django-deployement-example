from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'forapp/index.html')

def other(request):
    return render(request ,'forapp/other.html')
def rut(request):
    return render(request,'forapp/rut.html')
