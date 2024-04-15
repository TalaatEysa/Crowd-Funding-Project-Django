from django.shortcuts import render, redirect, reverse
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


def index(request):
    return render(request,'users/index.html')


def login_form(request):
    form=AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')

    return render(request,'users/login.html',{'form':form})


def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            login_url = reverse("index")
            return redirect(login_url)
    return render(request, 'users/register.html', {'form': form})


#
def user_details(request):
    # user = request.user
    first_user = User.objects.first()
    return render(request,'users/user_details.html',{'user': first_user} )

