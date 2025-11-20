from django.db import models

# Create your models here.
class Esrb_model(models.Model):
    clasificacion = models.CharField(max_length=50)
    logo= models.ImageField()
    def __str__(self):
        return self.clasificacion
    class Meta:
        db_table = 'esrb'

class Desarrolladora_model(models.Model):
    pais = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    logo = models.ImageField()
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'desarrolladora'

class Editora_model(models.Model):
    pais = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    logo = models.ImageField()
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'editora'

class Genero_model(models.Model):
    genero = models.CharField(max_length=50)
    def __str__(self):
        return self.genero
    class Meta:
        db_table = 'genero'

class Plataforma_model(models.Model):
    director = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    logo = models.ImageField()
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'plataforma'

class Titulo_model(models.Model):
    titulo = models.CharField(max_length=20)
    fecha_lanzamiento = models.DateField()
    precio = models.IntegerField()
    descripcion = models.TextField()
    etiquetas = models.CharField(max_length=50)
    portada = models.ImageField()
    plataforma = models.ForeignKey(Plataforma_model, on_delete=models.RESTRICT)
    desarrolladora  = models.ForeignKey(Desarrolladora_model, on_delete=models.RESTRICT)
    editora  = models.ForeignKey(Editora_model, on_delete=models.RESTRICT)
    esrb  = models.ForeignKey(Esrb_model, on_delete=models.RESTRICT)
    genero  = models.ForeignKey(Genero_model, on_delete=models.RESTRICT)
    def __str__(self):
        return self.titulo
    class Meta:
        db_table = 'juego'

class Resena_model(models.Model):
    fuente = models.CharField(max_length=50)
    puntuacion = models.IntegerField()
    fecha_resena = models.DateField()
    descripcion = models.TextField()
    def __str__(self):
        return self.fuente
    class Meta:
        db_table = 'resena'