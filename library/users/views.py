from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth

from users.forms import UserUpdateForm, CreateSuperUserForm,UserRegistrationForm

# Create your views here.
def logout(request):
    auth.logout(request)
    return render(request, "users/logout.html")


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'form': u_form
    }
    return render(request,'users/profile.html',context)

def createsuperuser(request):
    if request.method == 'POST':
        form = CreateSuperUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, You can Now login')
            return redirect('users-login')
    else:
        form = CreateSuperUserForm()
    return render(request, 'users/super.html', {'form': form})