from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'core/home.html')
def about(request):
    return render(request, 'core/about.html')
def store(request):
    return render(request, 'core/store.html')
def contact(request):
    return render(request, 'core/contact.html')

# Create your views here.
