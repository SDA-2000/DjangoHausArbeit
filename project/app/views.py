from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm, Register, Login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.urls import reverse

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
            return redirect(f"/me/{your_name}/")
    
def get2_endp_crud_read(request, username: str):
    if request.method == 'GET':
        users = User.objects.all()
        data = {"your_name" : username, "users" : users}
        return render(request, 'apply.html', data)

def login(request):
    if request.method == "POST":
        log_form = Login(request.POST)
        if log_form.is_valid():
            username = log_form.cleaned_data.get('username')
            password = log_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return redirect(f'accounts/profile/{username}')
            else:
                log_form.add_error(None, 'Invalid username or password')
    else:
        log_form = Login()
        data = {"log_form" : log_form}
        return render(request, 'login.html', data)


def registration(request):
    if request.method == "POST":
        reg_form = Register(request.POST)
        if reg_form.is_valid():
            new_user = reg_form.save(commit=False)
            new_user.set_password(reg_form.cleaned_data['password'])
            data = {"new_user" : new_user}

            new_user.save()
            return redirect('../login')
    else:
        reg_form = Register()
        data = {"reg_form" : reg_form}
        return render(request, 'register.html', data)

def change_user_data(request, username: str):
    user = User.objects.get(username=username)

    if request.method == 'GET':
        change_form = Register(instance=user)
        data = {"change_form" : change_form, "username" : username}
        return render(request, 'changing.html', data)

    if request.method == 'POST':
        change_form = Register(request.POST, instance=user)
        if change_form.is_valid():
            change_form.save()
            return redirect(f"/me?new_user={user}")

def delete_user(request, cur_username: str, username: str):
    if cur_username == username:
        return redirect(f"/me/{cur_username}/?yourself=True")
    user = User.objects.get(username=username)
    user.delete()
    return render(request,)