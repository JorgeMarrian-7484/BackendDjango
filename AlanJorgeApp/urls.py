from django.urls import path
from AlanJorgeApp.views import ESRB,crearESRB,Desarrolladora,crearDesarrolladora,Editora,crearEditora,Genero,crearGenero,Plataforma,crearPlataforma,Titulo_juego,crearTitulo, editarDesarrolladora, editarEditora, editarEsrb, editarGenero, editarPlataforma, editarResena, editarTitulo,resenas,crearResenas,eliminarTitulo,eliminarDesarrolladora,eliminarEditora,eliminarEsrb,eliminarGenero,eliminarPlataforma,eliminarResena,exportarExcel
urlpatterns = [
    # ESRB
    path('esrb/',ESRB,name='esrb'),
    path('cesrb/',crearESRB,name='crearesrb'),
    path('esrb/editar/<int:id>/', editarEsrb, name='editar_esrb'),
    path('esrb/eliminar/<int:id>/', eliminarEsrb, name='eliminar_esrb'),
    
    # DESARROLLADORA
    path('desarrolladoras/',Desarrolladora,name='desarrolladora'),
    path('cdesarrolladora/',crearDesarrolladora,name='creardesarrolladora'),
    path('desarrolladoras/editar/<int:id>/', editarDesarrolladora, name='editar_desarrolladora'),
    path('desarrolladoras/eliminar/<int:id>/', eliminarDesarrolladora, name='eliminar_desarrolladora'),
    
    # EDITORA
    path('editoras/',Editora, name='editora'),
    path('ceditora/',crearEditora, name = 'creareditora'),
    path('editoras/editar/<int:id>/', editarEditora, name='editar_editora'),
    path('editoras/eliminar/<int:id>/', eliminarEditora, name='eliminar_editora'),
    
    # GENERO
    path('generos/',Genero, name='genero'),
    path('cgenero/', crearGenero,name='creargenero'),
    path('generos/editar/<int:id>/', editarGenero, name='editar_genero'),
    path('generos/eliminar/<int:id>/', eliminarGenero, name='eliminar_genero'),
    
    # PLATAFORMA
    path('plataformas/',Plataforma,name='plataforma'),
    path('cplataforma/',crearPlataforma, name= 'crearplataforma'),
    path('plataformas/editar/<int:id>/', editarPlataforma, name='editar_plataforma'),
    path('plataformas/eliminar/<int:id>/', eliminarPlataforma, name='eliminar_plataforma'),
    
    # TITULO
    path('titulos/', Titulo_juego, name='titulojuego'),
    path('cjuego/',crearTitulo,name='crearjuego'),
    path('titulos/editar/<int:id>/', editarTitulo, name='editar_titulo'),
    path('titulos/eliminar/<int:id>/', eliminarTitulo, name='eliminar_titulo'),
    
    # RESEÑA
    path('resenas/',resenas, name='resenas'),
    path('cresenas/',crearResenas, name='crearresenas'),
    path('resenas/editar/<int:id>/', editarResena, name='editar_resena'),
    path('resenas/eliminar/<int:id>/', eliminarResena, name='eliminar_resena'),
    # exportar titulo
    path('juegosexcel/<str:texto>/<int:esrb>/<int:desarrolladora>/<int:editora>/<int:genero>/<int:plataforma>/<int:resenas>', exportarExcel)
]
