from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to the desired page after login
                return redirect('home')
            else:
                # Handle invalid login credentials
                pass
    else:
        form = AuthenticationForm()

    return render(request, 'custom_login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('custom_login')

def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('custom_login')
