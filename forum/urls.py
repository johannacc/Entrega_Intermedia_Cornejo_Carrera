from django.urls import path

from forum import views

app_name = "forum"
urlpatterns = [
    path("forum/", views.create_forum, name="forum-list"),
]
