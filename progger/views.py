from django.shortcuts import render, redirect

def home(request):
    title = "Progger"
    context = {'title': title}
    return render(request, 'progger/index.html', context)

def resume(request):
    return render(request, 'progger/resume.html') 
