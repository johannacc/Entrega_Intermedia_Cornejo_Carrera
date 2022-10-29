from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render


from my_app.forms import ViajeForm
from my_app.models import Viaje


def get_destinos(request):
   destinos = Viaje.objects.all()
   paginator = Paginator(destinos, 3)
   page_number = request.GET.get("page")
   return paginator.get_page(page_number)

def destinos(request):
    destinos = Viaje.objects.all()

    context_dict = {"destinos": destinos}

    return render(
        request=request,
        context=context_dict,
        template_name="my_app/destino_list.html",
    )

def create_destino(request):
   if request.method == "POST":
       destino_form = ViajeForm(request.POST)
       if destino_form.is_valid():
           data = destino_form.cleaned_data
           actual_objects = Viaje.objects.filter(
               name=data["name"],
               year=data["year"],
           ).count()
           print("actual_objects", actual_objects)
           if not actual_objects:
                destino = Viaje( 
                    name=data["name"],
                    year=data["year"],)
                destino.save()
                messages.success(
                    request,
                    f"Viaje a {data['name']} en {data['year']} agregado exitosamente!",
                )
                return render(
                    request=request,
                    context={"destino_list": get_destinos(request)},
                    template_name="my_app/destino_list.html",
                )

           else:
            messages.error(
                    request,
                    f"El viaje {data['name']} ya está ingresado.",
                )


   destino_form = ViajeForm(request.POST) 
   context_dict = {"form": destino_form}
   return render(
       request=request,
       context=context_dict,
       template_name="my_app/destino_form.html",
   )

