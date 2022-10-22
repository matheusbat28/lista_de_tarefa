import email
from django.shortcuts import redirect, render
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(email= email, senha=senha)

        if user == None:
            print('erro')
        else:
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'login/index.html')
