from django.shortcuts import render
from . models import Places
from . models import People
# Create your views here.
def index(request):
    obj = Places.objects.all()
    pop = People.objects.all()
    return render(request, 'index.html',{'result':obj,'output':pop})


# def result(request):
#     a = int(request.GET['number1'])
#     b = int(request.GET['number2'])
#     res = a + b
#     sub = a - b
#     pro = a * b
#     div = a / b
#     mod = a % b
#     return render(request, 'result.html',{'result':res,'subtraction':sub,'multi':pro,'division':div,'modulus':mod})