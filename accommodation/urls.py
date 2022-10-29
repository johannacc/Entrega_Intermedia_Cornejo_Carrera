from django.urls import path

from accommodation import views

app_name = "accommodation"
urlpatterns = [
    path("accommodations/", views.accommodations, name="accommodation-list"),
    #path("accommodation/add", views.create_accommodation, name="accommodation-add"),
]

