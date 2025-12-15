from django.shortcuts import redirect, render
from AlanJorgeApp.forms import ESRBForm,DesarrolladoraForm, EditoraForm,GeneroForm,PlataformaForm,TituloForm,ResenasForm, TituloFiltro
from AlanJorgeApp.models import Esrb_model,Desarrolladora_model, Editora_model,Genero_model,Plataforma_model,Titulo_model,Resena_model
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db.models import Count, Avg, Max, Min
import xlwt
from django.core.paginator import Paginator
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import io

# permisos de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

@login_required(login_url='accounts/login')
def inicio(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada, {username}! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@permission_required('AlanJorgeApp.view_ESRB',login_url='/')
def ESRB(request):
    esrb = Esrb_model.objects.all()
    data = {
        'titulo':'Clasificacion Por edad',
        'esrb': esrb
    }
    return render(request,'src/ESRB.html',data)
@permission_required('AlanJorgeApp.view_Desarrolladora',login_url='/')
def Desarrolladora(request):
     desarrolladora = Desarrolladora_model.objects.all()
     paginator = Paginator(desarrolladora,3)
     pageNum = request.GET.get('page')
     pageObj = paginator.get_page(pageNum)
     
     data = {
          'titulo': 'Desarrolladora',
          'desarrolladora':pageObj
     }
     return render(request,'src/Desarrolladoras.html',data)
@permission_required('AlanJorgeApp.view_Editora',login_url='/')
def Editora(request):
     editora = Editora_model.objects.all()
     paginator = Paginator(editora,2)
     pageNum = request.GET.get('page')
     pageObj = paginator.get_page(pageNum)
     data = {
          'titulo':'Editora',
          'editora': pageObj
     }
     return render(request,'src/Editoras.html',data)
@permission_required('AlanJorgeApp.view_Genero',login_url='/')
def Genero(request):
    genero = Genero_model.objects.all()
    paginator = Paginator(genero,3)
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    data = {
          'titulo': 'Genero',
          'genero': pageObj
    }
    return render(request,'src/Generos.html',data)
@permission_required('AlanJorgeApp.view_Plataforma',login_url='/')
def Plataforma(request):
     plataforma = Plataforma_model.objects.all()
     paginator = Paginator(plataforma,3)
     pageNum = request.GET.get('page')
     pageObj = paginator.get_page(pageNum)
     data = {
          'titulo':'Plataforma',
          'plataforma':pageObj
     }
     return render(request,'src/Plataforma.html',data)
@permission_required('AlanJorgeApp.view_Titulo_juego',login_url='/')
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
            juego = juego.filter(esrb = esrb)
         if desarrolladora != '':
            juego = juego.filter(desarrolladora=desarrolladora)
         if editora != '':
            juego = juego.filter(editora=editora)
         if genero != '':
            juego = juego.filter(genero=genero)
         if plataforma != '':
            juego = juego.filter(plataforma=plataforma)
         if resenas != '':
            juego = juego.filter(resenas=resenas)
     paginator = Paginator(juego,2)
     pageNum = request.GET.get('page')
     pageObj = paginator.get_page(pageNum)
     data = {
          'titulo':'Juegos',
          'juego':pageObj,
          'form': form
     }
     return render(request,'src/Juego.html',data)
@permission_required('AlanJorgeApp.view_resenas',login_url='/')
def resenas(request):
     resena = Resena_model.objects.all()
     paginator = Paginator(resena,3)
     pageNum = request.GET.get('page')
     pageObj = paginator.get_page(pageNum)
     data = {
          'titulo':'Reseñas',
          'resena':pageObj
     }
     return render(request,'src/Resenas.html',data)


# Funciones de creacion de datos
@permission_required('AlanJorgeApp.add_ESRB',login_url='/')
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
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, "Clasificacion creada correctamente")
            return redirect('esrb')
    else:
        form = ESRBForm()
    return render(request, 'src/Crear.html',data)
@permission_required('AlanJorgeApp.add_Desarrolladora',login_url='/')
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
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, "Desarrolladora creada correctamente")
            return redirect('desarrolladora')
    else:
        form = DesarrolladoraForm()
    return render(request, 'src/Crear.html',data)
@permission_required('AlanJorgeApp.add_Editora',login_url='/')
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
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, "Editora creada correctamente")
            return redirect('editora')
    else:
        form = EditoraForm()
    return render(request, 'src/Crear.html',data)
@permission_required('AlanJorgeApp.add_Genero',login_url='/')
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
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, "Genero creado correctamente")
            return redirect('genero')
    else:
        form = GeneroForm()
    return render(request, 'src/Crear.html',data)
@permission_required('AlanJorgeApp.add_Plataforma',login_url='/')
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
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, "Plataforma creada correctamente")
            return redirect('plataforma')
    else:
        form = PlataformaForm()
    return render(request, 'src/Crear.html',data)
@permission_required('AlanJorgeApp.add_Titulo_juego',login_url='/')
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
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, "Titulo creado correctamente")
            return redirect('titulojuego')
    else:
        form = TituloForm()
    return render(request, 'src/Crear.html',data)
@permission_required('AlanJorgeApp.add_resenas',login_url='/')
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
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, "Reseña creada correctamente")
            return redirect('resenas')
    else:
        form = ResenasForm()
    return render(request, 'src/Crear.html',data)
#ELIMINAR

def eliminarEsrb(request, id):
    esrb = Esrb_model.objects.get(pk=id)
    esrb.delete()
    return redirect('/src/esrb/')

def eliminarDesarrolladora(request, id):
    dev = Desarrolladora_model.objects.get(pk=id)
    dev.delete()
    return redirect('/src/desarrolladoras/')

def eliminarEditora(request, id):
    editora = Editora_model.objects.get(pk=id)
    editora.delete()
    return redirect('/src/editoras/')

def eliminarGenero(request, id):
    genero = Genero_model.objects.get(pk=id)
    genero.delete()
    return redirect('/src/generos/')

def eliminarPlataforma(request, id):
    plataforma = Plataforma_model.objects.get(pk=id)
    plataforma.delete()
    return redirect('/src/plataformas/')

def eliminarTitulo(request, id):
    titulo = Titulo_model.objects.get(pk=id)
    titulo.delete()
    return redirect('/src/titulos/')

def eliminarResena(request, id):
    resena = Resena_model.objects.get(pk=id)
    resena.delete()
    return redirect('/src/resenas/')

#EDITAR
@permission_required('AlanJorgeApp.change_ESRB',login_url='/')
def editarEsrb(request, id):
    esrb = Esrb_model.objects.get(pk=id)
    form = ESRBForm(instance=esrb)
    data = {
        'titulo': 'Editar Clasificación ESRB',
        'form': form,
        'ruta': '/src/esrb/'
    }
    if request.method == 'POST':
        form = ESRBForm(request.POST, request.FILES, instance=esrb)
        if form.is_valid():
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, 'ESRB actualizado con éxito!')
    return render(request, 'src/edit.html', data)
@permission_required('AlanJorgeApp.change_Desarrolladora',login_url='/')
def editarDesarrolladora(request, id):
    dev = Desarrolladora_model.objects.get(pk=id)
    form = DesarrolladoraForm(instance=dev)
    data = {
        'titulo': 'Editar Desarrolladora',
        'form': form,
        'ruta': '/src/desarrolladoras/'
    }
    if request.method == 'POST':
        form = DesarrolladoraForm(request.POST, request.FILES, instance=dev)
        if form.is_valid():
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, 'Desarrolladora actualizada con éxito!')
    return render(request, 'src/edit.html', data)
@permission_required('AlanJorgeApp.change_Editora',login_url='/')
def editarEditora(request, id):
    editora = Editora_model.objects.get(pk=id)
    form = EditoraForm(instance=editora)
    data = {
        'titulo': 'Editar Editora',
        'form': form,
        'ruta': '/src/editoras/'
    }
    if request.method == 'POST':
        form = EditoraForm(request.POST, request.FILES, instance=editora)
        if form.is_valid():
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, 'Editora actualizada con éxito!')
    return render(request, 'src/edit.html', data)
@permission_required('AlanJorgeApp.change_Genero',login_url='/')
def editarGenero(request, id):
    genero = Genero_model.objects.get(pk=id)
    form = GeneroForm(instance=genero)
    data = {
        'titulo': 'Editar Género',
        'form': form,
        'ruta': '/src/generos/'
    }
    if request.method == 'POST':
        form = GeneroForm(request.POST,request.FILES, instance=genero)
        if form.is_valid():
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, 'Género actualizado con éxito!')
    return render(request, 'src/edit.html', data)
@permission_required('AlanJorgeApp.change_Plataforma',login_url='/')
def editarPlataforma(request, id):
    plataforma = Plataforma_model.objects.get(pk=id)
    form = PlataformaForm(instance=plataforma)
    data = {
        'titulo': 'Editar Plataforma',
        'form': form,
        'ruta': '/src/plataformas/'
    }
    if request.method == 'POST':
        form = PlataformaForm(request.POST, request.FILES, instance=plataforma)
        if form.is_valid():
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, 'Plataforma actualizada con éxito!')
    return render(request, 'src/edit.html', data)
@permission_required('AlanJorgeApp.change_Titulo_juego',login_url='/')
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
            FileSystemStorage(location='media/juegos/')
            form.save()
            messages.success(request, 'Título actualizado con éxito!')
    return render(request, 'src/edit.html', data)
@permission_required('AlanJorgeApp.change_resenas',login_url='/')
def editarResena(request, id):
    resena = Resena_model.objects.get(pk=id)
    form = ResenasForm(instance=resena)
    data = {
        'titulo': 'Editar Reseña',
        'form': form,
        'ruta': '/src/resenas/'
    }
    if request.method == 'POST':
        form = ResenasForm(request.POST, instance=resena)
        if form.is_valid():
            FileSystemStorage(location='media/juegos/')
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

    columnas = ['Titulo','Fecha de lanzamiento','Precio','Genero','Plataforma', 'Desarrolladora', 'Editora','ESRB']
    for i in range(len(columnas)):
        hoja.write(row_num,i,columnas[i],font_style)

    font_style = xlwt.XFStyle()

    filas = Titulo_model.objects.all().values_list('titulo','fecha_lanzamiento','precio','genero__genero','plataforma__nombre','desarrolladora__nombre','editora__nombre','esrb__clasificacion')
    
    if texto != '0':
        filas = filas.filter(titulo__icontains=texto)
    if esrb != 0:
        filas = filas.filter(esrb=esrb)
    if desarrolladora != 0:
        filas = filas.filter(desarrolladora=desarrolladora)
    if editora != 0:
        filas = filas.filter(editora=editora)
    if genero != 0:
        filas = filas.filter(genero=genero)
    if plataforma != 0:
        filas = filas.filter(plataforma=plataforma)
    if resenas != 0:
        filas = filas.filter(resenas=resenas)
    
    for f in filas:
        row_num += 1
        for col_num in range (len(f)):
            hoja.write(row_num,col_num, str(f[col_num]), font_style)
    archivo.save(response)
    return response

def exportarPDF(request, texto, esrb, desarrolladora, editora, genero, plataforma, resenas):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="juegos.pdf"'
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    

    filas = Titulo_model.objects.all().values_list(
        'titulo', 'fecha_lanzamiento', 'precio', 'genero__genero', 
        'plataforma__nombre', 'desarrolladora__nombre', 
        'editora__nombre', 'esrb__clasificacion'
    )
    

    if texto != '0':
        filas = filas.filter(titulo__icontains=texto)
    if int(esrb) != 0:  
        filas = filas.filter(esrb=esrb)
    if int(desarrolladora) != 0:
        filas = filas.filter(desarrolladora=desarrolladora)
    if int(editora) != 0:
        filas = filas.filter(editora=editora)
    if int(genero) != 0:
        filas = filas.filter(genero=genero)
    if int(plataforma) != 0:
        filas = filas.filter(plataforma=plataforma)
    if int(resenas) != 0:
        filas = filas.filter(resenas=resenas)
    

    columnas = ['Título', 'Fecha Lanzamiento', 'Precio', 'Género', 
                'Plataforma', 'Desarrolladora', 'Editora', 'ESRB']
    
    data = [columnas]  
    
    for fila in filas:
        data.append([str(cell) if cell is not None else '' for cell in fila])
    
 
    if len(data) > 1:  
        table = Table(data)
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),  
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#ecf0f1')),  
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#bdc3c7')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')])
        ])
        table.setStyle(style)
        elements.append(table)
    else:
        from reportlab.lib.styles import getSampleStyleSheet
        styles = getSampleStyleSheet()
        elements.append(Paragraph("No se encontraron juegos con los filtros aplicados", styles['Heading2']))
    
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


@login_required
def dashboard(request):

    total_juegos = Titulo_model.objects.count()
    precio_promedio = Titulo_model.objects.aggregate(Avg('precio'))['precio__avg']
    precio_maximo = Titulo_model.objects.aggregate(Max('precio'))['precio__max']
    

    juegos_por_plataforma = Plataforma_model.objects.annotate(
        total_juegos=Count('titulo_model')
    )
    

    juegos_por_genero = Genero_model.objects.annotate(
        total=Count('titulo_model')
    ).order_by('-total')
    
    juegos_por_esrb = Esrb_model.objects.annotate(
        total=Count('titulo_model')
    )
    
    ultimos_juegos = Titulo_model.objects.order_by('-fecha_lanzamiento')[:5]
    
    context = {
        'total_juegos': total_juegos,
        'precio_promedio': round(precio_promedio, 2) if precio_promedio else 0,
        'precio_maximo': precio_maximo,
        'juegos_por_plataforma': juegos_por_plataforma,
        'juegos_por_genero': juegos_por_genero,
        'juegos_por_esrb': juegos_por_esrb,
        'ultimos_juegos': ultimos_juegos,
    }
    return render(request, 'src/dashboard.html', context)

def inicio(request):
    # SOLO esta línea - sin select_related
    juegos_destacados = Titulo_model.objects.all().order_by('-fecha_lanzamiento')[:8]
    
    context = {
        'juegos_destacados': juegos_destacados,
        'titulo_seccion': 'Juegos Destacados',
        'subtitulo': 'Los últimos títulos agregados'
    }
    return render(request, 'index.html', context)