from django.shortcuts import redirect, render
from AlanJorgeApp.forms import ESRBForm,DesarrolladoraForm, EditoraForm,GeneroForm,PlataformaForm,TituloForm,ResenasForm, TituloFiltro
from AlanJorgeApp.models import Esrb_model,Desarrolladora_model, Editora_model,Genero_model,Plataforma_model,Titulo_model,Resena_model
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import xlwt 
from django.http import HttpResponse

def inicio(request):
    return render(request,'index.html')

# Crear una secuencia de creacion para el titulo del juego, y la reseña se añade durante o despues de la creacion de la tabla
# Crear ESRB/Desarrolladora/Editora/Genero/Plataforma/Titulo/Reseñas
#Mostrar los elementos ingresados desde model.py

def ESRB(request):
    esrb = Esrb_model.objects.all()
    data = {
        'titulo':'Clasificacion Por edad',
        'esrb': esrb
    }
    return render(request,'src/ESRB.html',data)

def Desarrolladora(request):
     desarrolladora = Desarrolladora_model.objects.all()
     data = {
          'titulo': 'Desarrolladora',
          'desarrolladora':desarrolladora
     }
     return render(request,'src/Desarrolladoras.html',data)

def Editora(request):
     editora = Editora_model.objects.all()
     data = {
          'titulo':'Editora',
          'editora': editora
     }
     return render(request,'src/Editoras.html',data)

def Genero(request):
    genero = Genero_model.objects.all()
    data = {
          'titulo': 'Genero',
          'genero': genero
    }
    return render(request,'src/Generos.html',data)

def Plataforma(request):
     plataforma = Plataforma_model.objects.all()
     data = {
          'titulo':'Plataforma',
          'plataforma':plataforma
     }
     return render(request,'src/Plataforma.html',data)

def Titulo_juego(request):
     juego = Titulo_model.objects.all()
     form = TituloFiltro()
     if request.method == 'POST':
         form = TituloFiltro(request.POST)
         texto = request.POST.get('texto')
         esrb = request.POST.get('esrb')
         desarrolladora = request.POST.get('desarrolladora')
         editora = request.POST.get('editora')
         genero = request.POST.get('genero')
         plataforma = request.POST.get('plataforma')
         resenas = request.POST.get('resenas')
         if texto != '':
            juego = juego.filter(titulo__icontains=texto)
         if esrb != '':
            juego = juego.filter(esrb__id = esrb)
         if desarrolladora != '':
            juego = juego.filter()
     data = {
          'titulo':'Juegos',
          'juego':juego
     }
     return render(request,'src/Juego.html',data)

def resenas(request):
     resena = Resena_model.objects.all()
     data = {
          'titulo':'Reseñas',
          'resena':resena
     }
     return render(request,'src/Resenas.html',data)


# Funciones de creacion de datos

def crearESRB(request):
    form = ESRBForm()
    data = {
         'titulo':'Crear ESRB',
         'form': form,
         'ruta': '/src/esrb/'
    }

    if request.method == 'POST':
        form = ESRBForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Clasificacion creada correctamente")
            return redirect('esrb')
    else:
        form = ESRBForm()
    return render(request, 'src/Crear.html',data)

def crearDesarrolladora(request):
    form = DesarrolladoraForm()
    data = {
         'titulo':'Crear Desarrolladora',
         'form': form,
         'ruta': '/src/desarrolladora/'
    }
    if request.method == 'POST':
        form = DesarrolladoraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Desarrolladora creada correctamente")
            return redirect('desarrolladora')
    else:
        form = DesarrolladoraForm()
    return render(request, 'src/Crear.html',data)

def crearEditora(request):
    form = EditoraForm()
    data = {
        'titulo':'Crear Editora',
         'form': form,
         'ruta': '/src/editora/'
    }
    if request.method == 'POST':
        form = EditoraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Editora creada correctamente")
            return redirect('editora')
    else:
        form = EditoraForm()
    return render(request, 'src/Crear.html',data)

def crearGenero(request):
    form = GeneroForm()
    data = {
        'titulo':'Crear Genero',
         'form': form,
         'ruta': '/src/genero/'
    }
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Genero creado correctamente")
            return redirect('genero')
    else:
        form = GeneroForm()
    return render(request, 'src/Crear.html',data)

def crearPlataforma(request):
    form = PlataformaForm()
    data = {
         'titulo':'Crear Plataforma',
         'form': form,
         'ruta': '/src/plataforma/'
    }
    if request.method == 'POST':
        form = PlataformaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Plataforma creada correctamente")
            return redirect('plataforma')
    else:
        form = PlataformaForm()
    return render(request, 'src/Crear.html',data)

def crearTitulo(request):
    form = TituloForm()
    data = {
         'titulo':'Crear Titulo del juego',
         'form': form,
         'ruta': '/src/juego/'
    }
    if request.method == 'POST':
        form = TituloForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Titulo creado correctamente")
            return redirect('titulojuego')
    else:
        form = TituloForm()
    return render(request, 'src/Crear.html',data)

def crearResenas(request):
    form = ResenasForm()
    data = {
         'titulo':'Crear Reseñas',
         'form': form,
         'ruta': '/src/resenas/'
    }
    if request.method == 'POST':
        form = ResenasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Reseña creada correctamente")
            return redirect('resenas')
    else:
        form = ResenasForm()
    return render(request, 'src/Crear.html',data)
#ELIMINAR

def eliminarEsrb(request, id_esrb):
    esrb = Esrb_model.objects.get(pk=id_esrb)
    esrb.delete()
    return redirect('/src/esrb/')

def eliminarDesarrolladora(request, id_desarrolladora):
    dev = Desarrolladora_model.objects.get(pk=id_desarrolladora)
    dev.delete()
    return redirect('/src/desarrolladoras/')

def eliminarEditora(request, id_editoria):
    editora = Editora_model.objects.get(pk=id_editoria)
    editora.delete()
    return redirect('/src/editoras/')

def eliminarGenero(request, id_genero):
    genero = Genero_model.objects.get(pk=id_genero)
    genero.delete()
    return redirect('/src/generos/')

def eliminarPlataforma(request, id_plataforma):
    plataforma = Plataforma_model.objects.get(pk=id_plataforma)
    plataforma.delete()
    return redirect('/src/plataformas/')

def eliminarTitulo(request, id):
    titulo = Titulo_model.objects.get(pk=id)
    titulo.delete()
    return redirect('/src/titulos/')

def eliminarResena(request, id_resena):
    resena = Resena_model.objects.get(pk=id_resena)
    resena.delete()
    return redirect('/src/resenas/')

#EDITAR

def editarEsrb(request, id_esrb):
    esrb = Esrb_model.objects.get(pk=id_esrb)
    form = ESRBForm(instance=esrb)
    data = {
        'titulo': 'Editar Clasificación ESRB',
        'form': form,
        'ruta': '/src/esrb/'
    }
    if request.method == 'POST':
        form = ESRBForm(request.POST, request.FILES, instance=esrb)
        if form.is_valid():
            form.save()
            messages.success(request, 'ESRB actualizado con éxito!')
    return render(request, 'src/edit.html', data)

def editarDesarrolladora(request, id_desarrolladora):
    dev = Desarrolladora_model.objects.get(pk=id_desarrolladora)
    form = DesarrolladoraForm(instance=dev)
    data = {
        'titulo': 'Editar Desarrolladora',
        'form': form,
        'ruta': '/src/desarrolladoras/'
    }
    if request.method == 'POST':
        form = DesarrolladoraForm(request.POST, request.FILES, instance=dev)
        if form.is_valid():
            form.save()
            messages.success(request, 'Desarrolladora actualizada con éxito!')
    return render(request, 'src/edit.html', data)

def editarEditora(request, id_editoria):
    editora = Editora_model.objects.get(pk=id_editoria)
    form = EditoraForm(instance=editora)
    data = {
        'titulo': 'Editar Editora',
        'form': form,
        'ruta': '/src/editoras/'
    }
    if request.method == 'POST':
        form = EditoraForm(request.POST, request.FILES, instance=editora)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editora actualizada con éxito!')
    return render(request, 'src/edit.html', data)

def editarGenero(request, id_genero):
    genero = Genero_model.objects.get(pk=id_genero)
    form = GeneroForm(instance=genero)
    data = {
        'titulo': 'Editar Género',
        'form': form,
        'ruta': '/src/generos/'
    }
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            messages.success(request, 'Género actualizado con éxito!')
    return render(request, 'src/edit.html', data)

def editarPlataforma(request, id_plataforma):
    plataforma = Plataforma_model.objects.get(pk=id_plataforma)
    form = PlataformaForm(instance=plataforma)
    data = {
        'titulo': 'Editar Plataforma',
        'form': form,
        'ruta': '/src/plataformas/'
    }
    if request.method == 'POST':
        form = PlataformaForm(request.POST, request.FILES, instance=plataforma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Plataforma actualizada con éxito!')
    return render(request, 'src/edit.html', data)

def editarTitulo(request, id):
    titulo = Titulo_model.objects.get(pk=id)
    form = TituloForm(instance=titulo)
    data = {
        'titulo': 'Editar Título',
        'form': form,
        'ruta': '/src/titulos/'
    }
    if request.method == 'POST':
        form = TituloForm(request.POST, request.FILES, instance=titulo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Título actualizado con éxito!')
    return render(request, 'src/edit.html', data)

def editarResena(request, id_resena):
    resena = Resena_model.objects.get(pk=id_resena)
    form = ResenasForm(instance=resena)
    data = {
        'titulo': 'Editar Reseña',
        'form': form,
        'ruta': '/src/resenas/'
    }
    if request.method == 'POST':
        form = ResenasForm(request.POST, instance=resena)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reseña actualizada con éxito!')
    return render(request, 'src/edit.html', data)

def exportarExcel(request, esrb, desarrolladora, editora, genero, plataforma, resenas,texto):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=juegos.xls'
    archivo = xlwt.Workbook(encoding='utf-8')
    hoja = archivo.add_sheet('Juegos')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columnas = ['Titulo','Fecha de lanzamiento','Precio','Genero','Etiquetas','Plataforma', 'Desarrolladora', 'Editora','ESRB']
    for i in range(len(columnas)):
        hoja.write(row_num,i,columnas[i],font_style)

    font_style = xlwt.XFStyle()

    filas = Titulo_model.objects.all().values_list('titulo','fecha_lanzamiento','precio','descripcion','etiquetas','plataforma','desarrolladora','editora','genero')
    
    if texto != '0':
        filas = filas.filter(titulo__icontains=texto)
    if esrb != 0:
        filas = filas.filter(esrb__id=esrb)
    if desarrolladora != 0:
        filas = filas.filter(desarrolladora__id=desarrolladora)
    if editora != 0:
        filas = filas.filter(editora__id=editora)
    if genero != 0:
        filas = filas.filter(genero__id=genero)
    if plataforma != 0:
        filas = filas.filter(plataforma__id=plataforma)
    if resenas != 0:
        filas = filas.filter(resenas__id=resenas)
    
    for f in filas:
        row_num += 1
        for col_num in range (len(f)):
            hoja.write(row_num,col_num, str(f[col_num]), font_style)
    archivo.save(response)
    return response
    