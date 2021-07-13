from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Attorneys
from .forms import ContactForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about_us.html')

def attorneys(request):
    attorneys = Attorneys.objects.all()
    context = {'attorney': attorneys}
    return render(request, 'attorneys.html')    

def case_studies(request):
    return render(request, 'case_studies.html')

def blog(request):
    return render(request, 'blog.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'contact.html', {'form': form})

def testimonials(request):
    return render(request, 'testimonials.html')

def pricing(request):
    return render(request, 'pricing.html')

def practice_areas(request):
    return render(request, 'practice_areas.html')


