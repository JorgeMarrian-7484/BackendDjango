from django import forms
from AlanJorgeApp.models import Esrb_model, Desarrolladora_model,Genero_model,Titulo_model,Resena_model,Editora_model,Plataforma_model

# FORMULARIO ESRB
class ESRBForm(forms.ModelForm):
    class Meta:
        model = Esrb_model
        fields = '__all__'
        widgets = {
            'clasificacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: M (Mature), T (Teen), E (Everyone)'
            }),
            'logo': forms.FileInput(attrs={'class': 'form-select'})
        }
        

# FORMULARIO DESARROLLADORA
class DesarrolladoraForm(forms.ModelForm):
    class Meta:
        model = Desarrolladora_model
        fields = '__all__'
        widgets = {
            'pais': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Japón, EE.UU, Canadá...'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Nintendo, FromSoftware...'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-select',
                'rows': 3,
                'placeholder': 'Describe brevemente la desarrolladora'
            }),
            'logo': forms.FileInput(attrs={'class': 'form-select'})
        }

# FORMULARIO GENERO
class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero_model
        fields = '__all__'
        widgets = {
            'genero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Acción, RPG, Aventura...'
            })
        }

# FORMULARIO EDITORA
class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora_model
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Sega, Capcom, Activision...'
            }),
            'pais': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'País de origen'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-select',
                'rows': 3,
                'placeholder': 'Describe brevemente la editora'
            }),
            'logo': forms.FileInput(attrs={'class': 'form-select'})
        }

# FORMULARIO PLATAFORMA
class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma_model
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: PlayStation 5, PC, Nintendo Switch...'
            }),
            'logo': forms.FileInput(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-select',
                'rows': 3,
                'placeholder': 'Describe brevemente la plataforma'
            }),
            'director': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Director o responsable de la plataforma'
            }),
        }

# FORMULARIO TITULO
class TituloForm(forms.ModelForm):
    class Meta:
        model = Titulo_model
        fields = [
            'titulo', 'fecha_lanzamiento', 'precio', 'descripcion',
            'etiquetas', 'portada', 'plataforma', 'desarrolladora',
            'editora', 'esrb', 'genero'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del videojuego'
            }),
            'fecha_lanzamiento': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Ej: 49.99'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-select', 'rows': 3,
                'placeholder': 'Describe brevemente el videojuego'
            }),
            'etiquetas': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Multijugador, Indie, Fantasía...'
            }),
            'portada': forms.FileInput(attrs={'class': 'form-select'}),
            'plataforma': forms.Select(attrs={'class': 'form-select'}),
            'desarrolladora': forms.Select(attrs={'class': 'form-select'}),
            'editora': forms.Select(attrs={'class': 'form-select'}),
            'esrb': forms.Select(attrs={'class': 'form-select'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
        }

# FORMULARIO RESEÑA
class ResenasForm(forms.ModelForm):
    class Meta:
        model = Resena_model
        fields = '__all__'
        widgets = {
            'titulo': forms.Select(attrs={'class': 'form-select'}),
            'fuente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: IGN, Metacritic, Steam Reviews...'
            }),
            'puntuacion': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Ej: 8.5'
            }),
            'fecha_resena': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-select', 'rows': 3,
                'placeholder': 'Opinión o comentario de la reseña'
            })
        }

# Filtros para la pagina
# **Filtro por Titulo del videojuego** #
# Cada clase de filtro tiene que ir para cada categoria que tenemos creada
class TituloFiltro(forms.Form):
    # Filtro para el texto
    texto = forms.CharField(required=False,
                                    widget= forms.TextInput(attrs={'class':'form-control'}))
    #filtro por items
    esrb = forms.ModelChoiceField(queryset=Esrb_model.objects.all().order_by('clasificacion'),
                                    empty_label='Todas las clasificaciones', required=False, 
                                    widget=forms.Select(attrs={'class':'form-select'}))
    desarrolladora = forms.ModelChoiceField(queryset=Desarrolladora_model.objects.all().order_by('nombre'),
                                    empty_label='Todas las desarrolladoras', required=False, 
                                    widget=forms.Select(attrs={'class':'form-select'}))
    editora = forms.ModelChoiceField(queryset=Editora_model.objects.all().order_by('nombre'),
                                    empty_label='Todas las editoras', required=False, 
                                    widget=forms.Select(attrs={'class':'form-select'}))
    genero = forms.ModelChoiceField(queryset=Genero_model.objects.all().order_by('genero'),
                                    empty_label='Todos los generos', required=False, 
                                    widget=forms.Select(attrs={'class':'form-select'}))
    plataforma = forms.ModelChoiceField(queryset=Plataforma_model.objects.all().order_by('nombre'),
                                    empty_label='Todas las plataformas', required=False, 
                                    widget=forms.Select(attrs={'class':'form-select'}))
    resenas = forms.ModelChoiceField(queryset=Resena_model.objects.all().order_by('fuente'),
                                    empty_label='Todas las reseñas', required=False, 
                                    widget=forms.Select(attrs={'class':'form-select'}))


#Segun se entiende se puede utilizar solo un filtro para hacer todas las funciones de esta pagina de momento

# class EsrbFiltro(forms.Form):
#     texto = forms.ModelChoiceField(required=False,
#                                     widget= forms.TextInput(attrs={'class':'form-control'}))
#     desarrolladora = forms.ModelChoiceField(queryset=Desarrolladora_model.objects.all().order_by('nombre'),
#                                     empty_label='Todas las desarrolladoras', required=False, 
#                                     widget=forms.Select(attrs={'class':'form-select'}))
#     editora = forms.ModelChoiceField(queryset=Editora_model.objects.all().order_by('nombre'),
#                                     empty_label='Todas las editoras', required=False, 
#                                     widget=forms.Select(attrs={'class':'form-select'}))
#     genero = forms.ModelChoiceField(queryset=Genero_model.objects.all().order_by('genero'),
#                                     empty_label='Todos los generos', required=False, 
#                                     widget=forms.Select(attrs={'class':'form-select'}))
#     plataforma = forms.ModelChoiceField(queryset=Plataforma_model.objects.all().order_by('nombre'),
#                                     empty_label='Todas las plataformas', required=False, 
#                                     widget=forms.Select(attrs={'class':'form-select'}))
#     resenas = forms.ModelChoiceField(queryset=Resena_model.objects.all().order_by('fuente'),
#                                     empty_label='Todas las reseñas', required=False, 
#                                     widget=forms.Select(attrs={'class':'form-select'}))
#     titulo = forms.ModelChoiceField(queryset=Titulo_model.objects.all().order_by('titulo'),
#                                     empty_label='Todos los titulos')