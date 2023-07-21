from django.db import models


class Categoria(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name= 'Nombres')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50, verbose_name= 'Nombres')
    direccion = models.CharField(max_length=50, verbose_name= 'direccion')

    def __str__(self):
        return self.nombres


class Productos(models.Model):
    codigo = models.AutoField(primary_key=True)
    idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='idcategoria', verbose_name= 'idcategoria')
    nombre = models.CharField(max_length=50, verbose_name= 'nombre')
    fechavencimiento = models.DateField(null=False, verbose_name= 'fecha')
    precio = models.IntegerField( verbose_name= 'precio')

    def __str__(self):
        return self.nombre

class Vendedor(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50,verbose_name= 'Nombres')

    def __str__(self):
        return self.nombres
# Create your models here.
