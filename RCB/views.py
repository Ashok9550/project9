from django.shortcuts import render

# Create your views here.
def RCB(request):
    D={'captain':'virat','age':30}
    return render(request,'RCB.html',context=D)