from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'pages/index.html')

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            messages.success(request, 'Ďakujeme! Správa bola odoslaná.')
        else:
            messages.error(request, 'Prosím, vyplň všetky polia.')
        return redirect('home')
    return redirect('home')