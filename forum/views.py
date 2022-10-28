from django.shortcuts import render

from forum.models import Forum

def create_forum(request):
    create_forum = Forum.objects.all()

    context_dict = {"create_forum": create_forum}

    return render(
        request=request,
        context=context_dict,
        template_name="forum/forum_list.html",
    )
