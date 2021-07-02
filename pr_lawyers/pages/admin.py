from django.contrib import admin
from .models import Contact, Category, Case_study, Attorneys, Practice_areas

admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Case_study)
admin.site.register(Attorneys)
admin.site.register(Practice_areas)

