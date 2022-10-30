from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator
from forum.models import Forum


from forum.forms import ForumForm
from forum.models import Forum


def get_forum(request):
   forum = Forum.objects.all()
   paginator = Paginator(forum, 3)
   page_number = request.GET.get("page")
   return paginator.get_page(page_number)

def forum(request):
    return render(
        request=request,
        context={"forum_list": get_forum(request)},
        template_name="forum_list.html",
    )   
def create_forum(request):
   if request.method == "POST":
       forum_form = ForumForm(request.POST)
       if forum_form.is_valid():
           data = forum_form.cleaned_data
           actual_objects = Forum.objects.filter(
               name=data["name"], email=data["email"]
           ).count()
           print("actual_objects", actual_objects)
           if not actual_objects:
                forum = Forum( 
                    name=data["name"],
                    email=data["email"], )
                forum.save()
                messages.success(
                    request,
                    f"Su reseña {data['name']} se agregó exitosamente!",
                )
                return render(
                    request=request,
                    context={"forum_list": get_forum(request)},
                    template_name="forum/forum_list.html",
                )

           else:
            messages.error(
                    request,
                    f"Su reseña {data['name']} ya está registrada",
                )


   forum_form = ForumForm(request.POST) 
   context_dict = {"form": forum_form}
   return render(
       request=request,
       context=context_dict,
       template_name="forum/forum_form.html",
   )    
    
