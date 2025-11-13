from django.contrib import admin
from django.urls import path, include
from AlanJorgeApp.views import inicio
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inicio de la pagina web
    path('', inicio, name='inicio'),
    # Pagina principal de la aplicacion. Tienda es el nombre para referirse a la app
    path('src/',include('AlanJorgeApp.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)