from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm, Register

def get_endp(request):

    if request.method == 'GET':
        form = NameForm()

        data = {"form" : form} 
    
        return render(request, 'form.html', data)

    if request.method == 'POST':

        form = NameForm(request.POST)

        your_name = request.POST['your_name']

        data = {"your_name" : your_name}
        
        if form.is_valid():
            return redirect(f"/me?your_name={your_name}")
    
    
def get2_endp(request):
    if request.method == 'GET':
        your_name = request.GET.get('your_name')
        data = {"your_name" : your_name}
        return render(request, 'apply.html', data)

def registration(request):
    if request.method == "POST":
        reg_form = Register(request.POST)
        if reg_form.is_valid():
            new_user = reg_form.save(commit=False)
            new_user.set_password(reg_form.cleaned_data['password'])
            data = {"new_user" : new_user}

            new_user.save()
            return render(request, 'apply.html', data)
    else:
        reg_form = Register()
        data = {"reg_form" : reg_form}
        return render(request, 'register.html', data)
    

        
        

