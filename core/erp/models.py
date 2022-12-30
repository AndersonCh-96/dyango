from django.db import models
from datetime import datetime
# Create your models here.

class Type(models.Model):
    name=models.CharField(max_length=150,verbose_name="Nombre")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']



class Employee(models.Model):
    types=models.ForeignKey("Type", on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, verbose_name='Dni', unique=True)
    date_joined = models.DateField(
        default=datetime.now, verbose_name='Fecha de registro')
    date_created = models.DateField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    #gener=models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cv = models.FileField(upload_to='cv/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
