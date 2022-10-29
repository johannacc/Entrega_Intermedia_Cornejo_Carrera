from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render


from accommodation.forms import AccommodationForm
from accommodation.models import Accommodation


def get_accommodations(request):
   accommodations = Accommodation.objects.all()
   paginator = Paginator(accommodations, 3)
   page_number = request.GET.get("page")
   return paginator.get_page(page_number)

def accommodations(request):
    return render(
        request=request,
        context={"accommodation_list": get_accommodations(request)},
        template_name="accommodation/accommodation_list.html",
    )   


def create_accommodation(request):
   if request.method == "POST":
       accommodation_form = AccommodationForm(request.POST)
       if accommodation_form.is_valid():
           data = accommodation_form.cleaned_data
           actual_objects = Accommodation.objects.filter(
               name=data["name"]
           ).count()
           print("actual_objects", actual_objects)
           if not actual_objects:
                accommodation = Accommodation( 
                    name=data["name"])
                accommodation.save()
                messages.success(
                    request,
                    f"Alojamiento {data['name']} agregado exitosamente!",
                )
                return render(
                    request=request,
                    context={"accommodation_list": get_accommodations(request)},
                    template_name="accommodation/accommodation_list.html",
                )

           else:
            messages.error(
                    request,
                    f"El alojamiento {data['name']} ya está registrado",
                )


   accommodation_form = AccommodationForm(request.POST) 
   context_dict = {"form": accommodation_form}
   return render(
       request=request,
       context=context_dict,
       template_name="accommodation/accommodation_form.html",
   )







