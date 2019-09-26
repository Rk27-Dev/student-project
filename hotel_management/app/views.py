from django.shortcuts import render,redirect
from .forms import register_form
# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        form=register_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('succsess')
    else:
        form=register_form()
        return render(request,'register.html',{'form':form})
roomcost=""
def rooms(request):
    global roomcost
    roomcost=request.GET.get('r1')
    print(roomcost)
    return  render(request,'rooms.html')
foodcost=""
def food(request):
    global foodcost
    global roomcost
    foodcost=request.GET.get('f1')
    print(foodcost)
    return  render(request,'food.html')
def cost(request):
    global foodcost
    global roomcost
    total= foodcost+roomcost
    print(total)
    context={
        'total':total
    }
    return render(request,'home.html',context)

