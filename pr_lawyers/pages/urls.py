from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('attorneys/', views.attorneys, name="attorneys"),
    path('case_studies/', views.case_studies, name="case_studies"),
    path('blog/', views.blog, name="blog"),
    path('faq/', views.faq, name="faq"),
    path('contact/', views.contact, name="contact"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('pricing/', views.pricing, name="pricing"),
    path('practice_areas/', views.practice_areas, name="practice_areas"),
]