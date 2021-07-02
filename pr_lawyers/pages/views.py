from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about_us.html')

def attorneys(request):
    return render(request, 'attorneys.html')

def case_studies(request):
    return render(request, 'case_studies.html')

def blog(request):
    return render(request, 'blog.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def pricing(request):
    return render(request, 'pricing.html')

def practice_areas(request):
    return render(request, 'practice_areas.html')


