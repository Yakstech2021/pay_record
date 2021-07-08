from django import forms
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
# Create your views here.




def register(request):
    if request.method == 'POST':
       form = UserRegistrationForm(request.POST)
       if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        return redirect('login')

    else:
        form = UserRegistrationForm()

    return render(request, "registrations/UserRigistration.html", {'form':form})
    