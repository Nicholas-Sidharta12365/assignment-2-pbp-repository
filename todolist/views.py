from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from todolist.models import Task

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('wishlist:show_wishlist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('/todolist/login/')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/todolist/login/')
def todolist(request):

    tmp_user = request.user

    data = Task.objects.all().filter(user = tmp_user)

    context ={
        'username' : tmp_user.username,
        'taskData' : data,
    }

    return render(request, "todolist.html", context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def create_task(request):
    if request.method == 'POST':
        db = Task()
        db.user = request.user
        db.title = request.POST.get('title')
        db.description = request.POST.get('description')
        db.save()

        return redirect('todolist:todolist')

    return render(request, 'create-task.html')