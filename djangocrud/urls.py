from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluimos las urls que tenemos en la aplicacion tareas
    path('', include('tareas.urls'))
]
