from django.contrib import admin
from AlanJorgeApp.models import Desarrolladora_model, Plataforma_model, Editora_model, Titulo_model, Resena_model, Genero_model, Esrb_model
# Register your models here.

admin.site.register(Desarrolladora_model)
admin.site.register(Esrb_model)
admin.site.register(Plataforma_model)
admin.site.register(Editora_model)
admin.site.register(Genero_model)
admin.site.register(Titulo_model)
admin.site.register(Resena_model)