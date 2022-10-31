from django.shortcuts import render
from django.db.models import Q


from accommodation.models import Accommodation

def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )
def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(name__contains=search_param)
        query.add(Q(location__contains=search_param), Q.OR)
        accommodations = Accommodation.objects.filter(query)
        context_dict.update(
            {
                "accommodations": accommodations,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="accommodation/accommodation_list.html",
    )
