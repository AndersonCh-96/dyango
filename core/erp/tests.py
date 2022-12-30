from app.wsgi import *
from core.erp.models import Type,Employee

#Listar

query=Type.objects.all()
print(query)

#insertar

inserta=Type()
inserta.name="Prueba"
inserta.save()

#editar

inserta= Type.objects.get(id=1)
inserta="prueba"
inserta.save()

#eliminar
inserta= Type.objects.get(id=1)
inserta.delete()

#listar con filtro

filtra= Type.objects.filter(name__contains='Py').count()
filtra= Type.objects.filter(name__='Py')
print(filtra) 

#iterar
for i in  Type.objects.filter(name__contains='P'):
    print(i.name)

#con tablas relacionadas

empleado=Employee.objects.filter(types_id=2)
print(empleado)