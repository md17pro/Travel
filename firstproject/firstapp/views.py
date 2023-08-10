from django.http import HttpResponse
from django.shortcuts import render
from . models import place,team
# Create your views here.


def demo(request):
    obj=place.objects.all()
    obj2=team.objects.all()
    return render(request,'index.html',{'result':obj,'result2':obj2})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})