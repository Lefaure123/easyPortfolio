from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import KreyeKontForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.

def akey(request):
    context = {

    }
    return render(request, 'base.html', context)

def kreyeKont(request):
    if request.method == 'POST':
        form = KreyeKontForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            user = User.objects.create_user(username=last_name, password=password)
            user.save()
            print('everything is ok')
            return redirect(akey)
        else:
            print("fomile a pa valid")
            print(form.errors)
    else:    
        form = KreyeKontForm()

    context = {
            'form' : form,
        }
    return render(request, 'kreyekont.html', context)

def konekte(request):
    if request.method == "POST":
        form = KreyeKontForm(data=request.POST)
        if form.is_valid():
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password')
            user = authenticate(username=last_name, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Ou konekte antake {last_name}")
                return redirect(akey)
            else:
                messages.error(request, "Enfomasyon ou antre yo gen w ti pwoblem, reverifye")
        else:
            messages.error(request, "Enfomasyon ou antre yo gen ti pwoblem, reverifye")
    form = KreyeKontForm()
    return render(request=request, template_name="konekte.html", context = {'form': form})
