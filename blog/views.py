from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'home.html',{"data":"i'm xander"})
