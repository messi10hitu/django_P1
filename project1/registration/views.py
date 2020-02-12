from django.shortcuts import render
from . import forms
from .models import Register


# Create your views here.
def home(request):
    return render(request, 'registration/home.html')


def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)

        html = 'we have recieved this form again'
        if form.is_valid():
            firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone_no = form.cleaned_data['phone_no']
            age = form.cleaned_data['age']

            details = Register(first_name=firstName, last_name=lastName, email=email,
                               password=password, phone_no=phone_no,
                               age=age)  # these are models variable in red
            # process the data in form.cleaned_data as required
            details.save()
        html = html + ' this form is valid'
    else:
        html = 'welcome for first time'
    return render(request, 'registration/index.html', {'html': html, 'form': form})


def logform(request):
    form = forms.Login()
    if request.method == 'POST':
        form = forms.Login(request.POST)
        html = 'we have recieved this form again'
        if form.is_valid():
            html = html + ' this form is valid'
    else:
        html = 'welcome for first time'
    return render(request, 'registration/index.html', {'html': html, 'form': form})
