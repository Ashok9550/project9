from django.shortcuts import render

# Create your views here.
def CSK(request):
    D={'captain':'Dhoni','age':40}
    return render(request,'CSK.html',context=D)