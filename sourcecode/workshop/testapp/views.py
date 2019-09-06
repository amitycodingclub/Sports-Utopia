from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def create(request):
    return render(request,'acc.html')
def sport(request):
    return render(request,'sport.html')
def facilities(request):
    return render(request,'facilities.html')
