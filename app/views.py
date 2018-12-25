# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def new(request):
    return render(request,'new.html')

def newlist(request):
    return render(request,'newlist.html')

def share(request):
    return render(request,'share.html')