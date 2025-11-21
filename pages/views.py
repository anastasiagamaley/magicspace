from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'pages/index.html')

# --- DULA ---
def dula(request):
    return render(request, 'pages/dula.html')

def kontrakcie(request):
    return render(request, 'pages/kontrakcie.html')

def cerrada(request):
    return render(request, 'pages/cerrada.html')

def porodny_kurz(request):
    return render(request, 'pages/porodny_kurz.html')

# --- JOGA ---
def joga_martin(request):
    return render(request, 'pages/jogamartin.html')

def korp(request):
    return render(request, 'pages/korp.html')

# --- ABOUT & CONTACT ---
def o_mne(request):
    return render(request, 'pages/o_mne.html')

def kontakt(request):
    return render(request, 'pages/kontakt.html')

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