from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from twilio.rest import Client
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth import logout
from twilio.base.exceptions import TwilioRestException

from .forms import sms_form,sms_login_form
from django.contrib.auth.models import User
from .models import sms,sms_login
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
def home(request):
    count=User.objects.count()
    return render(request, 'registration/home.html', {'count':count})
def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            request.session.get_expiry_age(1500)
            form.save()
            return HttpResponse('succsessfull')
            # return render('/home')
    else:
        form=UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

def student_signup(request):
    if request.method=='POST':
        form=sms_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('succsessfull')
            # request.session.get_expiry_age(300)

            # return render('/')
    else:
        form=sms_form()

    return render(request, 'registration/student_signup.html', {'form':form})

def student_display(request):
    data=sms.objects.all()
    return render(request,'registration/student_display.html',{'data':data})
# def edit(request,id):
#     data = sms.objects.get(id=id)
#     return render(request, 'registration/student_display.html', {'data': data})
class studentUpdate(UpdateView):
    template_name = 'registration/sms_form.html'
    model = sms
    fields = ['name','message','ph_no','username','password']
    success_url = reverse_lazy('edit')

# class studentDelete(DeleteView):
#     model = sms
#     template_name = 'registration/sms_confirm_delete.html'
#     success_url = reverse_lazy('delete')

def studentDelete(request, id):
    student= get_object_or_404(sms, id=id)
    student.delete()
    return render(request, 'registration/sms_confirm_delete.html')

def student_login(request):
    if request.method == 'POST':
        form = sms_login_form(request.POST)
        if form.is_valid():
            e = form.cleaned_data['username']
            p=form.cleaned_data['password']
            ravi=sms.objects.filter(username=e,password=p)
            if not ravi:
                return HttpResponse('login failed')
            else:
                account_sid = 'AC3a846e5983cc3d62b4c303813b605241'
                auth_token = 'd66ca53f3f3ada42adf222a420a70fda'
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body='ur login is succsessfull!!..thanks for login',
                    from_='+12056276621',
                    to='+91-9533558978'
                )
                print(message.sid)

                return render(request, 'registration/home.html', {'form': ravi})
        else:
            return form.errors

        # return HttpResponse('msg succsessfull')
    else:
        form=sms_login_form()
        return  render(request,'registration/student_login.html',{'form':form})


from django.db.models import Q
def search(request):
	if request.method == 'POST':
		Emp = request.POST['frm']
		if Emp:
			form1 = sms.objects.filter(Q(name__icontains=Emp) | Q(ph_no__icontains=Emp) | Q(username__contains=Emp))
			if form1:
				return render(request,"registration/search.html",{'sr':form1})
			else:
				messages.error(request,"no result found")
		else:
			return HttpResponseRedirect('/search/')
	return render(request,"registration/search.html")

from twilio.rest import Client

def hello(request):
    account_sid = 'AC3a846e5983cc3d62b4c303813b605241'
    auth_token = 'd66ca53f3f3ada42adf222a420a70fda'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body='This is the ship that made the Kessel Run in fourteen parsecs?',
             from_='+12056276621',
             to='+91-9533558978'
         )
    print(message.sid)
    return HttpResponse('msg succsessfull')
