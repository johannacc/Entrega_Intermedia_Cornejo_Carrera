from django.shortcuts import render

from my_app.models import Viaje

def destinos(request):
    destinos = Viaje.objects.all()

    context_dict = {"destinos": destinos}

    return render(
        request=request,
        context=context_dict,
        template_name="my_app/destino_list.html",
    )
