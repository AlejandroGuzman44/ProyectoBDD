from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('' , views.inicio , name= 'inicio'), 
    path('nosotros' , views.nosotros , name = 'nosotros'),
    path('hoteles' , views.hoteles , name = 'hoteles'),
    path('hoteles/crear' , views.crear , name = 'crear'),
    path('hoteles/editar' , views.editar , name = 'editar'),
    path('eliminar <int:id>' , views.eliminar , name = 'eliminar'),
    path('hoteles/editar/ <int:id>' , views.editar , name = 'editar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)