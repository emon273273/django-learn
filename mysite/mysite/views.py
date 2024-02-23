from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name='emon'

    context={
        'name':'emonsab',
        'age':22,
        'nationality':'bangladeshi'
    }
    # return render(request,'index.html',{'name':name,})

    return render(request,'index.html',context)
