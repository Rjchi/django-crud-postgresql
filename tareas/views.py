# 0- Para verlo desde interfaz Win + Q editor del registro, HKEY_CLASSES_ROOT, .js
# 0-1 Content Type, application/javascript o desde la shell:
# 1- Desde el SQL Shell ejecutar \s para ver las credenciales y \d (para ver las tablas creadas) \d nom_tabla
# 2- Crear una nueva base de datos
# 3- Ejecutar pip install psycopg2 (esto es un controlador de Python para PostgreSQL)
# 4- Intalamos el formatiador para python ejecutando -m pip install -U autopep8
# 5- Creamos el modelo de la tabla para nuestra base de datos
# 6- Ejecutamos las migraciones a la base de datos con python manage.py makemigrations
# 7- Ejecutar python manage.py migrate le decimos que tome la migracion y empiece la creacion de la tabla
# 8- Ejecutamos python manage.py runserver (puerto) opcional ingresar el puerto
# 9- Vamos a las urls del nucleo del proyecto e incluimos las que tenemos en la aplicacion
# 9.1- Creamos las templates
# 10- crear las vistas
# 11- Añadir path con url y llamado a las vistas
# 12- Creamos el formulario para las templates

from django.shortcuts import render, redirect
from . import models


def index(request):
    return render(request, 'index.html')


def list_t(request):
    tareas = models.tareas.objects.all()  # Retorna una lista
    return render(request, 'list_tasks.html', {
        'tareas': tareas
    })


def create_task(request):
    # print(request.POST) # Mostramos lo que viene en el request (en los inputs del formulario) ver en la terminal

    # Aqui le pasamos lo que viene en el request y lo guardamos en un diccionario
    tarea = models.tareas(
        titulo=request.POST['titulo'], descripcion=request.POST['descripcion'])
    tarea.save()  # Y aqui lo guardamos en la base de datos
    return redirect('tasks')  # Redireccionamos a list_t


def delete(request, task_id):
    tarea = models.tareas.objects.get(
        id=task_id)  # Nos devuelve un diccionario
    tarea.delete()  # Y con esto lo borramos de la base de datos
    return redirect('tasks')  # Redireccionamos nuevamente al formulario


def edit(request, task_id):
    tarea = models.tareas.objects.get(id=task_id)
    return render(request, 'update.html', {
        'tarea': tarea
    })

def update(request, task_id):
    tarea = models.tareas.objects.get(id=task_id)
    tarea.titulo = request.POST['titulo']
    tarea.descripcion = request.POST['descripcion']
    tarea.save()
    return redirect('tasks')