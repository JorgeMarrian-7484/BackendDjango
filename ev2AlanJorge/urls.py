from django.contrib import admin
from django.urls import path, include
from AlanJorgeApp.views import inicio,register  
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inicio de la pagina web
    path('', inicio, name='inicio'),
    # Pagina principal de la aplicacion. Tienda es el nombre para referirse a la app
    path('src/',include('AlanJorgeApp.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    
