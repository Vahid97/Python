from django.urls import path
from pages.views import home
app_name = "pages"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home")
    
]