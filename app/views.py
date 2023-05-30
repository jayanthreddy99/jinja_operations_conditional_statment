from django.shortcuts import render

# Create your views here.
def condition(request):
    d = {'a':60,'b':30}
    return render(request,'condition.html',context=d)
