from django.shortcuts import redirect, render
from .models import Hotel
from .forms import HotelForm
# Create your views here.


#-------------------------------------------------------------------------------------------------------------------------------------


def inicio(request):
    return render(request , 'paginas/inicio.html')



def nosotros(request):
    return render(request , 'paginas/nosotros.html')


# ------------------------------------------------OBTENEMOS TODOS LOS HOTELES----------------------------------------------------------


def hoteles(request):
    hoteles = Hotel.objects.all()

    context = {
        "hoteles" : hoteles
    }

    return render(request , 'hoteles/index.html' , context )



# ------------------------------------------------CREAMOS EL HOTEL----------------------------------------------------------------------



def crear(request):
    formulario = HotelForm(request.POST or None , request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('hoteles')

    context = {
        "formulario":formulario
    }

    return render(request , 'hoteles/crear.html' , context)



# ------------------------------------------------EDITAMOS LOS HOTELES----------------------------------------------------------



def editar(request , id):

    hotel = Hotel.objects.get(id=id)
    formulario = HotelForm(request.POST or None , request.FILES or None , instance=hotel)

    context = {
        "formulario":formulario
    }

    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('hoteles')

    return render(request , 'hoteles/editar.html' , context)



# ------------------------------------------------ELIMINAMOS LOS HOTELES----------------------------------------------------------



def eliminar(request , id):
    hotel = Hotel.objects.get(id=id)
    hotel.delete()
    return redirect('hoteles')