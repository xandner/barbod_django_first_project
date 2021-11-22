from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'home.html',{"data":"i'm xander"})
def about(request):
    return render(request,'about.html')